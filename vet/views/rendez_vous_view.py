from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from vet.models import Rendez_vous
from django.shortcuts import get_object_or_404
from datetime import datetime, timedelta, time
from pytz import utc

# Create your views here.
def index(request):
    return render(request, "rendez_vous/rendez_vous_libre/affichage_date_libre.html")

def demande_de_rendez_vous(request):
    rendez_vous = Rendez_vous()
    tous_les_rendez_vous = rendez_vous.obtenir_demande_rendez_vous()
    return render(request, "rendez_vous/rendez_vous_interaction/demande_de_rendez_vous.html", { "tous_les_rendez_vous" : tous_les_rendez_vous})

def accepter_rendez_vous(request, id_rendez_vous):
    rendez_vous = Rendez_vous()
    rendez_vous = rendez_vous.rendez_vous_à_supprimer(id_rendez_vous)
    rendez_vous.etat = 0
    rendez_vous.save()
    return redirect("/vet/demande_de_rendez_vous")

def recherche_date_libre(request):
    if request.method == "POST":
        rendez_vous = Rendez_vous()
        date_debut = request.POST.get("date_debut")
        date_fin = request.POST.get("date_fin")
        date_debut = datetime.fromisoformat(date_debut)
        date_fin = datetime.fromisoformat(date_fin)
        date_occupées = rendez_vous.dates_libres(date_debut, date_fin)
        return render(request, "rendez_vous/rendez_vous_libre/affichage_date_libre.html", { 'date_occupées': date_occupées, 'date_fin' : date_fin, 'date_debut' : date_debut})    
    return render(request, "rendez_vous/rendez_vous_libre/affichage_date_libre.html")

def supprimer_rendez_vous(request, id_rendez_vous):
    rendez_vous = Rendez_vous()
    rendez_vous = rendez_vous.rendez_vous_à_supprimer(id_rendez_vous)
    return render(request, "rendez_vous/rendez_vous_libre/supprimer_rendez_vous.html", { "rendez_vous" : rendez_vous})

def confirmation_suppression(request, id_rendez_vous):
    rendez_vous = Rendez_vous()
    rendez_vous = rendez_vous.rendez_vous_à_supprimer(id_rendez_vous)
    rendez_vous.etat = 1
    rendez_vous.save()
    return redirect("/vet/")

def rendez_vous_entre_deux_dates(request):
    date_debut = request.POST.get("date_debut")
    date_fin = request.POST.get("date_fin")
    rendez_vous = Rendez_vous.rendez_vous_entre_dates(date_debut, date_fin)
    return render(request, "rendez_vous/rendez_vous_libre/affichage_date_libre.html", { 'rendez_vous': rendez_vous })

def annulation_suppression(request):
    return redirect("/vet/")

#safidy

def get_all_rendezvous(request):
    rendez_vous = Rendez_vous()
    rendezvous = rendez_vous.get_all_rendezvous()#.get_all_rendezvous()
    return render(request, "rendez_vous/rendez_vous_interaction/all_rendezvous.html", { 'rendez_vous_entre_2_dates': Rendez_vous.objects.all() })  

def get_rendez_vous_by_date_get(request, date_choisie):
    rendez_vous = Rendez_vous()
    date_string = date_choisie
    date = datetime.strptime(date_string, '%d-%m-%Y')
    rendez_vous = rendez_vous.get_all_rendez_vous_by_date(date)#.get_all_rendezvous()
    return render(request, "rendez_vous/rendez_vous_interaction/liste_rendez_vous.html", { 'rendez_vous_entre_2_dates': rendez_vous })    

def get_rendez_vous_by_date(request):
    rendez_vous = Rendez_vous()
    date = request.POST.get('date')
    date = datetime.fromisoformat(date)#.replace(tzinfo=utc)
    rendez_vous = rendez_vous.get_all_rendez_vous_by_date(date)#.get_all_rendezvous()
    return render(request, "rendez_vous/rendez_vous_interaction/liste_rendez_vous.html", { 'rendez_vous_entre_2_dates': rendez_vous })

def rendez_vous_entre_2_dates(request):
    date_debut=request.POST.get('date_debut')
    date_fin=request.POST.get('date_fin')
    date_debut = datetime.fromisoformat(date_debut).replace(tzinfo=utc)
    date_fin = datetime.fromisoformat(date_fin).replace(tzinfo=utc)
    rendez_vous=Rendez_vous()
    rendez_vous_entre_2_dates=rendez_vous.rendez_vous_entre_2_dates(date_debut, date_fin)
    return render(request, "rendez_vous/rendez_vous_interaction/all_rendezvous.html",{ 'rendez_vous_entre_2_dates': rendez_vous_entre_2_dates, "date_fin": date_fin, "date_debut": date_debut  })

def modifier_rendez_vous(request, id_rendez_vous):
    rendez_vous = Rendez_vous()
    rendez_vous = rendez_vous.rendez_vous_à_supprimer(id_rendez_vous)
    return render(request, "rendez_vous/rendez_vous_libre/modifier_rendez_vous.html", { "rendez_vous" : rendez_vous})

def traitement_modification(request):
    duree = request.POST.get('duree')
    id_rendez_vous = request.POST.get('id')
    date_prise = request.POST.get('date_prise')
    raison = request.POST.get('raison')

    date_prise = datetime.fromisoformat(date_prise).replace(tzinfo=utc)
    
    rendez_vous = Rendez_vous.objects.get(pk=id_rendez_vous)
    rendez_vous.date_de_prise = date_prise
    rendez_vous.date_fin = date_prise + timedelta(hours=int(duree))
    rendez_vous.raison = raison
    rendez_vous.save()
    return redirect("/vet/")

def date_selectionnee(request):
    if request.method == 'POST':
        date_clicked = request.POST.get('date_clicked')
        rendez_vous=Rendez_vous()
        liste_rendez_vous = rendez_vous.get_all_rendez_vous_by_date(date_clicked)
        return render(request, "rendez_vous/rendez_vous_interaction/liste_rendez_vous.html", { 'rendez_vous_entre_2_dates': liste_rendez_vous })
    else :
        return JsonResponse({'error': 'Invalid method, use POST instead.'},status=400)

    
