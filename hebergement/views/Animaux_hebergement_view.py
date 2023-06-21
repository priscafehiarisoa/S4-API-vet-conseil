from django.http import HttpResponse
from django.shortcuts import render

def Add_new_type_animals(request):
    return render(request,"hebergement/Ajouter_Animaux.html")

def show_list_hosted_animals(request):
    return render(request,"hebergement/animaux_hebergees.html")

def show_list_animals_that_can_be_hosted(request):
    return render(request,"hebergement/liste_animaux_hebergement.html")