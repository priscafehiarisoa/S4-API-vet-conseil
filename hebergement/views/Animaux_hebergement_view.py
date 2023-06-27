from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from hebergement.models import Animal_accepte
from hebergement.models.race import Race


def Add_new_type_animals(request):
    races = Race.objects.all()
    context = {'races': races}
    return render(request, "hebergement/animaux/Ajouter_Animaux.html", context)


# cette fonction va pouvoir héberger
def show_list_hosted_animals(request):
    if request.method == 'POST':
        date_value_test=request.POST.get('date_test')
        animal=Animal_accepte.objects.filter(debut_interval_validite=date_value_test)
        context = {'animal': animal}

    return render(request, "hebergement/hebergement/liste_animaux_hebergees.html",context)

#page temporaire test
def show_datetest(request):
    return render(request, "hebergement/hebergement/testdate.html")
def show_list_animals_that_can_be_hosted(request):
    return render(request, "hebergement/animaux/liste_animaux_on_peut_heberger.html")

def traiter_formulaire(request):
    if request.method == 'POST':
        race_value = request.POST.get('race_animal')
        age_debut_value = request.POST.get('debut_age')
        age_fin_value = request.POST.get('fin_age')
        debut_validite_value = request.POST.get('debut_validite')
        fin_validite_value = request.POST.get('fin_validite')


        # Créez une instance de la classe et attribuez les valeurs
        animal = Animal_accepte()
        animal.race_id = race_value
        animal.debut_interval_age = age_debut_value
        animal.fin_interval_age = age_fin_value
        animal.debut_interval_validite = debut_validite_value
        animal.fin_interval_validite = fin_validite_value

        # Enregistrez l'instance dans la base de données
        animal.save()

        # Redirigez vers une autre vue ou affichez un message de confirmation
        return redirect('load_hosting_managemment')
    return render(request,"hebergement/animaux/Ajouter_Animaux.html" )

