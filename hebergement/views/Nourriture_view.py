from django.http import HttpResponse
from django.shortcuts import render

def load_list_animals_food(request):
    return render(request, "hebergement/nourriture/liste_nourriture.html")

def add_new_type_food(request):
    return render(request, "hebergement/nourriture/ajouter_nourriture.html")