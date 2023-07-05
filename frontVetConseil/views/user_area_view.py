from django.http import HttpResponse
from django.shortcuts import render, redirect
from globale.models import Client
import json
from django.core.exceptions import ValidationError

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
    return render(request, "site/user/user_accueil.html")

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
    return render(request, "site/user/user_accueil.html")