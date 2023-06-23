from django.http import HttpResponse
from django.shortcuts import render

def Add_new_type_animals(request):
    return render(request, "hebergement/animaux/Ajouter_Animaux.html")


# cette fonction va pouvoir héberger
def show_list_hosted_animals(request):
    return render(request, "hebergement/hebergement/liste_animaux_hebergees.html")

def show_list_animals_that_can_be_hosted(request):
    return render(request, "hebergement/animaux/liste_animaux_on_peut_heberger.html")

