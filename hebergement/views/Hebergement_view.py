from datetime import datetime

from django.utils import timezone
from rest_framework.utils import json

from hebergement.forms import Date_validation_form, Ajouter_hebergement_form, Modifier_tarif_form
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from hebergement.models import Reservation, Details_reservation, Validation_reservation, Tarifs_Hebergement, Attribution


# gestion des hebergements
def load_hosting_managemment(request):
    formulaire = Date_validation_form()
    nombre_hebergement_attentes = Reservation.objects.filter(etat=10).count()
    nombre_reservations = Reservation.objects.filter(etat=20, date_fin__gt=datetime.now().date()).count()
    context = {"form": formulaire, 'nombre_hebergement_attente': nombre_hebergement_attentes,
               'nombre_reservations': nombre_reservations}
    return render(request, "hebergement/hebergement/Gestion_hebergement.html", context)


def load_hosting_managemments(request, form):
    formulaire = form
    nombre_hebergement_attentes = Reservation.objects.filter(etat=10).count()
    nombre_reservations = Reservation.objects.filter(etat=20, date_fin__gt=datetime.now().date()).count()
    context = {"form": formulaire, 'nombre_hebergement_attente': nombre_hebergement_attentes,
               'nombre_reservations': nombre_reservations}
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
        title = "client : " + d_reservation.reservation.client.nom, " | patient : ", d_reservation.patient.nom
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
            if(date_fin<date_debut):
                formulaire.add_error("date_debut","la date de fin be peux pas être antérieure au début")
                return load_hosting_managemments(request,formulaire)
            if (reservations.count() >= 10):
                res = "les dates sélectionnées " + str(date_debut) + " et " + str(date_fin) + " ne sont pas valides "
                return load_hosting_managemments(request, formulaire)
            else:
                res = "les dates sélectionnés " + str(date_debut) + " et " + str(
                    date_fin) + " sont libres "
                return load_hosting_managemments(request, formulaire)
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
            tarif_horaire = form.cleaned_data['tarif_journalier']
            frequence_medicaments = form.cleaned_data['frequence_medicament']
            okay = True

            # verifications de la validité des dates
            is_date_available = check_date(date_debut, date_fin)
            # verifications si la nourriture choisie n'est pas adapté a l'animal
            is_adapted_food = Attribution.check_if_available(animal.nature_id, nourriture)
            # verification si l'animal appartient au client
            is_owned_by_client = animal.check_if_owned_by_client(client)
            # redirections
            if not is_date_available or not is_adapted_food or not is_owned_by_client:
                if not is_owned_by_client:
                    form.add_error('client', 'le patient sélectionné n\'appartient pas au client')
                if not is_date_available:
                    form.add_error('date_debut_hebergement', 'la date n\'est pas libre ou bien elle n\'est pas valide')
                if not is_adapted_food:
                    form.add_error('type_nourriture', 'l\'aliment sélectionnée ne correspond pas au patient')

                okay = False
                return render(request, 'hebergement/hebergement/ajout_hebergement/ajout_hebergement.html',
                              {'form': form})
            if okay:
                reservation = Reservation()
                reservation.etat = 10
                reservation.client = client
                reservation.date_debut = date_debut
                reservation.date_fin = date_fin
                reservation.prix = calcul_prix(reservation, animal, quantite, frequence_nourriture, nourriture,
                                               tarif_horaire)
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
    form.initial['race'] = tarif.race.designation
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
                    tarif = Tarifs_Hebergement.objects.get(id=id_tarif)
                    tarif.montant_horaire = montant_horaire
                    tarif.montant_journalier = montant_journalier
                    tarif.save()
                except:
                    print(form.errors)

                return redirect('load_tarifs')
            else:
                print(">> ", form.errors)
        except:
            print(form.errors)
    else:
        form = Modifier_tarif_form()

    return render(request, 'hebergement/tarifs/modifier_tarif.html', {'form': form})


# validations
def check_date(date_debut, date_fin):
    isa = Reservation.objects.filter(
        Q(date_debut__range=(date_debut, date_fin)) | Q(date_fin__range=(date_debut, date_fin)), etat=20).count() < 10
    if (date_debut > date_fin):
        return False
    if isa >= 10:
        return False
    return True


def calcul_prix(reservation, patient, quantite_nourriture, frequence_nourriture, nourriture, is_tarif_horaire):
    # patient =Patient()
    tarifs = Tarifs_Hebergement.objects.filter(race=patient.nature).first()
    tarif = 0
    prix_hebergement = 0
    # calcul prix hebergement
    if (is_tarif_horaire):
        tarif = tarifs.montant_horaire.__float__()
        quantité_heure = (reservation.date_fin - reservation.date_debut).total_seconds() // 3600
        prix_hebergement = quantité_heure * tarif
    else:
        tarif = tarifs.montant_journalier.__float__()
        quantite_jour = (reservation.date_fin - reservation.date_debut).days
        prix_hebergement = tarif * quantite_jour

        # calcul prix nourriture
    prix_nourriture = (nourriture.prix_par_unite * (quantite_nourriture * frequence_nourriture)) / nourriture.unite

    return prix_nourriture + prix_hebergement
