from django.urls import include, path

from hebergement.views import test, Hebergement_view,Nourriture_view,Animaux_hebergement_view

urlpatterns = [
#   hebergement_view
    path('new_hosting_request',Hebergement_view.add_new_hosting_request,name="add_new_hosting_request"),
    path('hosting_management', Hebergement_view.load_hosting_managemment, name="load_hosting_managemment"),
    path("",Hebergement_view.load_hosting_managemment, name="load_hosting_managemment"),
    path('hosting_management/<str:allowed>', Hebergement_view.load_hosting_managemments, name="load_hosting_managemments"),
    path('check_date',Hebergement_view.check_if_valid_date,name="check_if_valid_date"),
    path('get_reservation',Hebergement_view.get_reservations,name="get_reservations"),
    path('list_animals',Hebergement_view.get_list_animals_for_date,name="get_list_animals_for_date"),

    # information hebergement
    path('hosting_informations',Hebergement_view.load_hosting_informations,name="load_hosting_informations"),

    # tarifs
    path('tarifs',Hebergement_view.load_tarifs,name="load_tarifs"),
    path('tarifs_modifier/<int:id_tarif>',Hebergement_view.modify_tarifs,name="modify_tarif"),
    path('modify_tarif_view',Hebergement_view.modifier_tarif_view,name="modifier_tarif_view"),
    # reservation
    path('hosting_reservation',Hebergement_view.load_hosting_reservation,name="load_hosting_reservation"),
    path('cancel_hosting/<int:id_obj>',Hebergement_view.cancel_hosting, name="cancel_hosting"),


    # demandes d'hebergement
    path('hosting_request',Hebergement_view.load_hosting_request,name="load_hosting_request"),
    path('accept_request/<int:id>',Hebergement_view.accept_request,name="accept_request"),
    path('reject_request/<int:id>',Hebergement_view.reject_request,name="reject_request"),


#   animaux
    path('new_type_animal',Animaux_hebergement_view.Add_new_type_animals,name="Add_new_type_animals") ,
    path('list_hosted_animals',Animaux_hebergement_view.show_list_hosted_animals,name="show_list_hosted_animals"),
    path('list_hosted_animal',Animaux_hebergement_view.show_list_hosted_animal,name="show_list_hosted_animal"),
    path('list_can_be_hosted_animals',Animaux_hebergement_view.show_list_animals_that_can_be_hosted,name="show_list_animals_that_can_be_hosted"),
    path('new_form_animals',Animaux_hebergement_view.traiter_formulaire,name="traiter_formulaire"),
    path('animaux_calendrier',Animaux_hebergement_view.animaux_calendrier,name="animaux_calendrier"),
    path('animaux_calendrier/<int:race_id>',Animaux_hebergement_view.show_animaux_calendrier,name="show_animaux_calendrier"),

    path('redirect_calendar_to_list_hosted_animals/<str:date_value_test>',Animaux_hebergement_view.redirect_calendar_to_list_hosted_animals,name='redirect_calendar_to_list_hosted_animals'),

#     nourriture
    path('list_foods',Nourriture_view.load_list_animals_food,name="load_list_animals_food"),
    path('new_food',Nourriture_view.add_new_type_food,name="add_new_type_food"),






]