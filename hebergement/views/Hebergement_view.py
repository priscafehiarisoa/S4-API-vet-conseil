from django.http import HttpResponse
from django.shortcuts import render

def load_hosting_managemment(request):
    return render(request, "hebergement/hebergement/Gestion_hebergement.html")

def load_hosting_informations(request):
    return render(request, "hebergement/hebergement/informations_hebergement.html")

def load_hosting_reservation(request):
    return render(request, "hebergement/hebergement/reservations_hebergement.html")

def load_hosting_request(request):
    return render(request, "hebergement/hebergement/demandes_hebergement.html")