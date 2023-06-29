from datetime import datetime

from django.utils import timezone
from rest_framework.utils import json

from hebergement.forms import Date_validation_form, Ajouter_hebergement_form, Modifier_tarif_form
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from hebergement.models import Reservation, Details_reservation, Validation_reservation, Tarifs_Hebergement


# gestion des hebergements
def load_hosting_managemment(request):
    formulaire = Date_validation_form()
    nombre_hebergement_attentes= Reservation.objects.filter(etat=10).count()
    context = {"form": formulaire, 'nombre_hebergement_attente':nombre_hebergement_attentes}
    return render(request, "hebergement/hebergement/Gestion_hebergement.html", context)


def load_hosting_managemments(request, allowed):
    formulaire = Date_validation_form()
    nombre_hebergement_attentes = Reservation.objects.filter(etat=10).count()
    context = {"form": formulaire, 'nombre_hebergement_attente': nombre_hebergement_attentes,"allowed": allowed}
    return render(request, "hebergement/hebergement/Gestion_hebergement.html",
                  context)


def get_reservations(request):
    detail_reservations = Details_reservation.objects.all()

    events = []
    for d_reservation in detail_reservations:
        # en attente
        if d_reservation.reservation.etat == 10:
            background_color = '#F5BEBD'
        #     validé
        elif d_reservation.reservation.etat == 20:
            background_color = '#1979EC'

        #     annulé
        elif d_reservation.reservation.etat == -10:
            background_color = '#F47174'
        else:
            background_color = 'gray'  # Default color for other etat values
        title = d_reservation.reservation.client.nom, " | ", d_reservation.patient.nom
        event = {
            'title': title,
            'start': d_reservation.reservation.date_debut.isoformat(),
            'end': d_reservation.reservation.date_fin.isoformat(),
            'backgroundColor': background_color,
        }
        events.append(event)

    return JsonResponse(events, safe=False)


def get_list_animals_for_date(request):
    if request.method == 'POST':
        # todo mettre une condition pour relier au formulaire crée par jeddy
        # on obtient la requette venant du json
        dict = json.loads(request.body)
        print(dict['date'])
        response_data = {'message': 'Date received successfully'}
        return JsonResponse(dict)


# verification de la validité des dates
def check_if_valid_date(request):
    if request.method == 'POST':
        formulaire = Date_validation_form(request.POST)
        if formulaire.is_valid():
            date_debut = formulaire.cleaned_data['date_debut']
            date_fin = formulaire.cleaned_data['date_fin']
            print(date_debut, date_fin)
            reservations = Reservation.objects.filter(
                Q(date_debut__range=(date_debut, date_fin)) | Q(date_fin__range=(date_debut, date_fin)),
                etat=20
            )
            if (reservations.count() >= 10):
                res = "les dates sélectionnées "+ str(date_debut)+" et "+str(date_fin)+" ne sont pas valides "
                return load_hosting_managemments(request, res)
            else:
                res = "les dates sélectionnés "+ str(date_debut)+" et "+str(date_fin)+" sont libres : il reste "+ (10-reservations.count()).__str__()+" place(s)"
                return load_hosting_managemments(request, res)
    else:
        formulaire = Date_validation_form()
        return load_hosting_managemment(request)
    return load_hosting_managemment(request)


def load_hosting_informations(request):
    return render(request, "hebergement/hebergement/informations_hebergement.html")


# GERER LES RESERVATIONS
def load_hosting_reservation(request):
    current_date = datetime.now().date()
    reservation = Details_reservation.objects.filter(reservation__etat=20, reservation__date_debut__gt=current_date)
    return render(request, "hebergement/hebergement/reservations_hebergement.html", {"reservation": reservation})


def cancel_hosting(request, id_obj):
    res = Reservation.objects.get(id=id_obj)
    res.etat = -10
    res.save()
    return load_hosting_reservation(request)


# GERER LES DEMANDES D'HEBERGEMENTS
# initialisation de la page
def load_hosting_request(request):
    demande = Details_reservation.objects.filter(reservation__etat=10)
    return render(request, "hebergement/hebergement/demandes_hebergement.html", {"reservation": demande})


def accept_request(request, id):
    reservation = Reservation.objects.get(id=id)
    reservation.etat = 20
    reservation.save()
    validation = Validation_reservation()
    validation.reservation = reservation
    validation.save()
    return load_hosting_request(request)


def reject_request(request, id):
    reservation = Reservation.objects.get(id=id)
    reservation.etat = 0
    reservation.save()
    return load_hosting_request(request)


# ajouter une demande d'hebergement

def add_new_hosting_request(request):
    if request.method == 'POST':
        form = Ajouter_hebergement_form(request.POST)
        if form.is_valid():
            client = form.cleaned_data['client']
            animal = form.cleaned_data['animal']
            date_debut = form.cleaned_data['date_debut_hebergement']
            date_fin = form.cleaned_data['date_fin_hebergement']
            nourriture = form.cleaned_data['type_nourriture']
            quantite = form.cleaned_data['quantite']
            frequence_nourriture = form.cleaned_data['frequence_nourriture']
            medicaments = form.cleaned_data['medicaments']
            frequence_medicaments = form.cleaned_data['frequence_medicament']

            reservation = Reservation()
            reservation.etat = 10
            reservation.client = client
            reservation.date_debut = date_debut
            reservation.date_fin = date_fin
            # todo mila calculer-na ny prix
            reservation.prix = reservation.calcul_prix()
            reservation.date_de_prise = timezone.now().date()
            reservation.save()

            detail_reservation = Details_reservation()
            detail_reservation.reservation = reservation
            detail_reservation.medicaments = medicaments
            detail_reservation.patient = animal
            detail_reservation.nourriture = nourriture
            detail_reservation.frequence = frequence_medicaments
            detail_reservation.save()

        #     todo mila ampidirina le frequence ana nourriture io
    else:
        form = Ajouter_hebergement_form()
    return render(request, 'hebergement/hebergement/ajout_hebergement/ajout_hebergement.html', {'form': form})


def load_tarifs(request):
    tarif = Tarifs_Hebergement.objects.all()
    return render(request, 'hebergement/tarifs/details_tarifs.html', {'tarif': tarif})


def modify_tarifs(request, id_tarif):

    tarif = Tarifs_Hebergement.objects.get(id=id_tarif)
    form = Modifier_tarif_form()
    form.initial['id_race'] = tarif.race_id
    form.initial['id_tarif'] = tarif.id
    form.initial['montant_horaire'] = tarif.montant_horaire
    form.initial['montant_journalier'] = tarif.montant_journalier
    form.initial['race']=tarif.race.designation
    return render(request, 'hebergement/tarifs/modifier_tarif.html', {'form': form})

def modifier_tarif_view(request):
    if request.method == 'POST':
        form = Modifier_tarif_form(request.POST)
        try:
            print(form.is_valid())
            if form.is_valid():
                try:
                    id_tarif = form.cleaned_data['id_tarif']
                    montant_journalier = form.cleaned_data['montant_journalier']
                    montant_horaire = form.cleaned_data['montant_horaire']
                    tarif=Tarifs_Hebergement.objects.get(id=id_tarif)
                    tarif.montant_horaire=montant_horaire
                    tarif.montant_journalier=montant_journalier
                    tarif.save()
                except:
                    print(form.errors)

                return redirect('load_tarifs')
            else:
                print(">> ",form.errors)
        except:
            print(form.errors)
    else:
        form = Modifier_tarif_form()

    return render(request, 'hebergement/tarifs/modifier_tarif.html', {'form': form})


# verifications des dates




