from django.shortcuts import render, redirect
from vet.models import Tarif_rendez_vous

def nouveau_tarif(request):

    tarifs = Tarif_rendez_vous.objects.order_by('-date_application')[:10][::-1]
    labels = []
    valeurs = []
    
    for tarif in tarifs:
        labels.append(tarif.date_application.strftime("%Y-%m-%d"))  # Formattez la date
        valeurs.append(tarif.valeur)
    

    prix_actuel = 0
    if(len(valeurs) > 0):
        prix_actuel = valeurs[len(valeurs) - 1]
    context = {
        'tarifs': tarifs,
        'labels': labels,
        'valeurs': valeurs,
        'prix_actuel': prix_actuel
    }
    
    return render(request, "rendez_vous/tarif_crud/nouveau_tarif.html", context)

def inserer_tarif(request):
    prix_ = request.POST.get("prix")
    date_ = request.POST.get("date")
    tarif = Tarif_rendez_vous()
    tarif.valeur = prix_
    tarif.date_application = date_
    tarif.save()
    return redirect("/vet/nouveau_tarif")