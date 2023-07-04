from django.urls import path

from vet.views import rendez_vous_view, tarif_view
from vet.views import Inserer_rendez_vous

urlpatterns = [
    #ce premier path va referencier l'url mysite/ à la vue nommée index
    path("", rendez_vous_view.index, name="index"),
    path("recherche_date_libre", rendez_vous_view.recherche_date_libre, name="recherche_date_libre"),
    path("supprimer_rendez_vous/<int:id_rendez_vous>", rendez_vous_view.supprimer_rendez_vous, name="supprimer_rendez_vous"),
    path("modifier_rendez_vous/<int:id_rendez_vous>", rendez_vous_view.modifier_rendez_vous, name="modifier_rendez_vous"),
    path("traitement_modification", rendez_vous_view.traitement_modification, name="traitement_modification"),
    path("confirmation_suppression/<int:id_rendez_vous>", rendez_vous_view.confirmation_suppression, name="confirmation_suppression"),
    path("rendez_vous_entre_deux_dates", rendez_vous_view.rendez_vous_entre_deux_dates, name="rendez_vous_entre_deux_dates"),
    path("annulation_suppression", rendez_vous_view.annulation_suppression, name="annulation_suppression"),
    path("calendar", rendez_vous_view.get_all_rendezvous, name="calendar"),
    path("by_2_date/", rendez_vous_view.rendez_vous_entre_2_dates, name="by_2_date"),
    path("by_1_date/",rendez_vous_view.get_rendez_vous_by_date, name="by_1_date"),
    path("date_selectionnee/",rendez_vous_view.get_rendez_vous_by_date, name="date_selectionnee"),
    path("Nouveau_rendez_vous", Inserer_rendez_vous.nouveau, name="Nouveau_rendez_vous"),
    path("Inserer_rendez_vous", Inserer_rendez_vous.Inserer_rendez_vous, name="Inserer_rendez_vous"),
    path("Ajouter_a_ces_date/<str:date_de_prise>/<str:date_fin>/", Inserer_rendez_vous.ajouter_a_ces_date, name="ajouter_a_ces_date"),
    path("nouveau_tarif", tarif_view.nouveau_tarif, name="nouveau_tarif"),
    path("inserer_tarif", tarif_view.inserer_tarif, name="inserer_tarif"),
    path("Nouveau_rendez_vous_pour_jour/<str:date_choisie>", Inserer_rendez_vous.nouveau_pour_jour, name="Nouveau_rendez_vous_pour_jour"),
    path("rendez_vous_date_clicked/<str:date_choisie>", rendez_vous_view.get_rendez_vous_by_date_get, name="Nouveau_rendez_vous_date_clicked"),
    path("demande_de_rendez_vous", rendez_vous_view.demande_de_rendez_vous, name="Demande_de_rendez_vous"),
    path("accepter_rendez_vous/<int:id_rendez_vous>", rendez_vous_view.accepter_rendez_vous, name="Demande_accepter_rendez_vous"),
]