from django.urls import include, path

from hebergement.views import test, Hebergement_view,Nourriture_view,Animaux_hebergement_view

urlpatterns = [
    path("", test.index, name="index"),
    # hebergement_view
    path('hosting_management', Hebergement_view.load_hosting_managemment, name="load_hosting_managemment"),
    path('hosting_informations',Hebergement_view.load_hosting_informations,name="load_hosting_informations"),
    path('hosting_reservation',Hebergement_view.load_hosting_reservation,name="load_hosting_reservation"),
    path('hosting_request',Hebergement_view.load_hosting_request,name="load_hosting_request"),


#   animaux
    path('new_type_animal',Animaux_hebergement_view.Add_new_type_animals,name="Add_new_type_animals") ,
    path('list_hosted_animals',Animaux_hebergement_view.show_list_hosted_animals,name="show_list_hosted_animals"),
    path('list_can_be_hosted_animals',Animaux_hebergement_view.show_list_animals_that_can_be_hosted,name="show_list_animals_that_can_be_hosted"),
    path('traiter_formulaire',Animaux_hebergement_view.traiter_formulaire,name="traiter_formulaire"),
    path('show_datetest',Animaux_hebergement_view.show_datetest,name="show_datetest"),
#     nourriture
    path('list_foods',Nourriture_view.load_list_animals_food,name="load_list_animals_food"),
    path('new_food',Nourriture_view.add_new_type_food,name="add_new_type_food"),
]