from django.urls import path
from frontVetConseil.views import user_area_view

urlpatterns = [
    path("", user_area_view.index, name="index"),
    path("login", user_area_view.login, name="login"),
    path("authentification", user_area_view.authentification, name="authentification"),
    path("inscription", user_area_view.inscription, name="inscription"),
    path("save", user_area_view.save, name="save"),
    path("ajout_patient", user_area_view.ajout_patient, name="ajout_patient"),
    path("demande_rendez_vous", user_area_view.demande_rendez_vous, name="demande_rendez_vous"),
    path("demande_hebergement", user_area_view.demande_hebergement, name="demande_hebergement"),
    path("inserer_rendez_vous", user_area_view.inserer_rendez_vous, name="inserer_rendez_vous"),
]