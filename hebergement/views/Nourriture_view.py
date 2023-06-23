from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render

from hebergement.models import  Attribution
from hebergement.models import Race

def load_list_animals_food(request):
    id_race = request.GET.get('id_race')

    races = Race.objects.all()
    if id_race == None:
        race = Race.objects.get(id=1)
        attributions = Attribution.objects.filter(race= race);
        return render(request, "hebergement/liste_nourriture.html", {"attributions": attributions, "races": races})

    else:
        race = Race.objects.get(id=id_race)
        attributions = Attribution.objects.filter(race= race);
        return render(request, "hebergement/liste_nourriture.html", {"attributions": attributions, "races":races})




def add_new_type_food(request):
    return render(request,"hebergement/ajouter_nourriture.html")