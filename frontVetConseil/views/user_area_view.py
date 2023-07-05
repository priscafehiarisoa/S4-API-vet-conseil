from django.http import HttpResponse
from django.shortcuts import render, redirect
from globale.models import Client, Patient, Race
from vet.models import Tarif_rendez_vous, Rendez_vous
import json
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta
from django.db.models import Q


from django.utils import timezone

from django.core.exceptions import ValidationError

from hebergement.forms import Ajouter_hebergement_user_form 
from django import forms
from hebergement.models import Reservation, Attribution, Details_reservation

def traitement_demande_hebergement (request):
    cid_lient = request.session.get("client")['id']
    client = Client.objects.get(id=cid_lient)
    if request.method == "POST":
        form = Ajouter_hebergement_user_form(client, data=request.POST)
        if form.is_valid():
            animal = form.cleaned_data["animal"]
            date_debut = form.cleaned_data["date_debut_hebergement"]
            date_fin = form.cleaned_data["date_fin_hebergement"]
            nourriture = form.cleaned_data["type_nourriture"]
            quantite   = form.cleaned_data["quantite" ]
            frequence_nourriture = form.cleaned_data["frequence_nourriture"]
            medicaments=form.cleaned_data["medicaments"]
            
          #  tarif_horaire=form.cleaned_data["tarif_horaire"]
            frequence_medicaments=form.cleaned_data["frequence_medicament"]
             # verifications de la validité des dates
            is_date_available = check_date(date_debut, date_fin)
            # verifications si la nourriture choisie n'est pas adapté a l'animal
            is_adapted_food = Attribution.check_if_available(animal.nature_id, nourriture)
            if not is_date_available or not is_adapted_food:
                if not is_date_available:
                    form.add_error('date_debut_hebergement', 'la date n\'est pas libre ou bien elle n\'est pas valide')
                if not is_adapted_food:
                    form.add_error('type_nourriture', 'l\'aliment sélectionnée ne correspond pas au patient')
                okay = False
           
            reservation = Reservation()
            reservation.etat = 10
            reservation.client = client
            reservation.date_debut = date_debut
            reservation.date_fin = date_fin
            reservation.prix = 10000
            reservation.date_de_prise = timezone.now().date()
            reservation.save()

            detail_reservation = Details_reservation()
            detail_reservation.reservation = reservation
            detail_reservation.medicaments = medicaments
            detail_reservation.patient = animal
            detail_reservation.nourriture = nourriture
            detail_reservation.frequence = frequence_medicaments
            detail_reservation.save()
    return redirect("demande_hebergement")

# validations
def check_date(date_debut, date_fin):
    isa = Reservation.objects.filter(
        Q(date_debut__range=(date_debut, date_fin)) | Q(date_fin__range=(date_debut, date_fin)), etat=20).count() < 10
    if (date_debut > date_fin):
        return False
    if isa >= 10:
        return False
    return True


def demande_rendez_vous(request):
    id_client = request.session.get('client')['id']
    client = Client.objects.get(id=id_client)
    patients = Patient.objects.filter(proprietaire=client)
    return render(request, 'site/user/demande_rendez_vous.html', {'patients': patients})
    
def inserer_rendez_vous(request):
    tarif = Tarif_rendez_vous.objects.latest('id')
    # obtenir l'id du patient
    client = request.POST.get('client')
    patient = Patient.objects.get(pk=client)

    motif = request.POST.get('raison')
    date_prise = request.POST.get('date_prise')
    date_consultation = request.POST.get('date_consultation')
    duree = request.POST.get('duree')
    date_prise = datetime.fromisoformat(date_prise)
    date_consultation = datetime.fromisoformat(date_consultation)
    rendez_vous = Rendez_vous()
    rendez_vous.date_de_prise = date_prise
    rendez_vous.date_fin = date_prise + timedelta(hours=int(duree))
    rendez_vous.date_consultation = date_consultation
    rendez_vous.raison = motif
    rendez_vous.patient = patient
    rendez_vous.etat = 2 # en attente de
    rendez_vous.prix= tarif.valeur * float(duree)
    rendez_vous.temps=10    
    rendez_vous.duree=duree
    try:
        rendez_vous.check_demande()
        #rendez_vous.save()
    except ValidationError as e:
        error_messages = e.message
        id_client = request.session.get('client')['id']
        client = Client.objects.get(id=id_client)
        patients = Patient.objects.filter(proprietaire=client)
        context = { 'patients' : patients, "error" : error_messages}
        return render(request, 'site/user/demande_rendez_vous.html', context)
    return redirect("/frontVetConseil/demande_rendez_vous")

def demande_hebergement(request):
    id_client = request.session.get('client')['id']
    print(id_client)
    client = Client.objects.get(id=id_client)
    #patient = Patient.objects.filter(proprietaire_id=client.id)
    form = Ajouter_hebergement_user_form(client)
    return render(request, 'site/user/demande_hebergement.html',  {'form': form})

def ajout_patient(request):
    if request.method == 'POST':
        client = request.session.get('client')
        id_race = request.POST.get('nature')    
        race = Race.objects.get(id=id_race)
        age = request.POST.get('age')
        nom = request.POST.get('nom')
        patient = Patient()
        patient.nature = race
        patient.nom = nom
        patient.age = age
        patient.proprietaire = Client.objects.get(id=client['id'])
        patient.save()
        races = Race.objects.all()
        return render(request, "site/user/user_accueil.html", { "races": races})
    else:
        return render(request, 'insert_patient1.html', {"client_id":client_id})  # Supposons que vous avez un modèle appelé 'save_patient.html'

def index(request):
    return render(request, "site/index.html")

def inscription(request):
    return render(request, "site/sign_in.html")

def login(request):
    return render(request, "site/login.html")

def save(request):
    client = Client()
    client.nom = request.POST.get('nom')
    client.prenom = request.POST.get('prenom')
    client.adresse = request.POST.get('adresse')
    client.mail = request.POST.get('email')
    client.contact = request.POST.get('contact')
    client.facebook = request.POST.get('facebook')
    client.password = request.POST.get('password')
    try:
        client.checkClient()
    except ValidationError as v_e:
        return render(request, "site/sign_in.html", {"error": v_e})
    client.save()
    json_data = client.jsonClient()
    request.session['client'] = json_data
    races = Race.objects.all()
    return render(request, "site/user/user_accueil.html", { "races": races})

def authentification(request):
    client = Client()

    client.mail = request.POST.get('email')
    client.password = request.POST.get('password')
    client = client.authentification()
    if client is None:
        return render(request, "site/login.html")
    #json_data = json.dumps(client)
    json_data = client.jsonClient()
    request.session['client'] = json_data
    races = Race.objects.all()
    return render(request, "site/user/user_accueil.html", { "races": races })