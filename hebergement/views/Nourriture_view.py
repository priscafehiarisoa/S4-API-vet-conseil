from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from django.contrib import messages

from hebergement.models import  Attribution
from globale.models import Race
from hebergement.models import Nourriture


def load_list_animals_food(request):
    id_race = request.GET.get('id_race')
    races = Race.objects.all()

    if id_race == None:
        race = Race.objects.first()
    else:
        try:
            race = Race.objects.get(id=id_race)
        except Race.DoesNotExist:
            pass

    attributions = Attribution.objects.filter(race=race);
    return render(request, "hebergement/nourriture/liste_nourriture.html", {"attributions": attributions, "races":races})




def add_new_type_food(request):
    description = request.GET.get('description')
    designation = request.GET.get('designation')
    prix_par_unite = request.GET.get('prix_unite')
    unite = request.GET.get('unite')
    if(description != None):
        try:
            new_food = Nourriture(designation=designation, description=description, prix_par_unite=prix_par_unite,
                                  unite=unite)
            new_food.save()
            new_food_id = new_food.id

            if request.method == 'GET':
                races_selectionnees = request.GET.getlist('attribution_checkbox')
                debut_interval_poids = 0
                fin_interval_poids = 100

                nourriture = Nourriture.objects.get(id=new_food_id)

                for race_id in races_selectionnees:
                    race = Race.objects.get(id=race_id)
                    attribution = Attribution(nourriture=nourriture, race=race,
                                              debut_interval_poids=debut_interval_poids,
                                              fin_interval_poids=fin_interval_poids)
                    attribution.save()
            messages.success(request, "Insertion réussie !!")

        except Exception as e:
            messages.error(request, "Echec de l'opération.")


    races = Race.objects.all()
    return render(request,"hebergement/nourriture/ajouter_nourriture.html", {"races": races})