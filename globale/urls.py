"""
URL configuration for entreprise project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.shortcuts import redirect
from django.urls import path
from globale.views import *





urlpatterns = [
    path('form_insert_race',form_insert_race, name='form_insert_race'),
    path('save_race',save_race, name='save_race'),
    path('race/<int:idRace>/delete',delete_race, name='delete_race'), #supprimer race
    path('race/<int:idRace>/modify',modify_race, name='modify_race'), #modifier race
    path('liste_race',list_race, name='liste_race'),


    path('form_insert_client',form_insert_client, name='form_insert_client'),
    path('select_client',select_client, name='liste_client'),
    path('save_client',save_client, name='save_client'),
    path('client/<int:idClient>/modify',modify_client,name='modify_client'),

    path('form_insert_poste',form_insert_poste, name='form_insert_poste'), #miditra amn insertion ana poste
    path('save_poste',save_poste, name='save_poste'), #save poste
    path('liste_poste',liste_poste, name='liste_poste'), #lister les postes
    path('poste/<int:idPoste>/delete',delete_poste, name='delete_poste'), #supprimer poste
    path('poste/<int:idPoste>/modifier',modify_poste, name='modify_poste'), #modifier poste
    path('poste/<int:idPoste>/detail',detail_poste, name='detail_poste'),#detailler poste modifée
    path('form_insert_personnel',form_insert_personnel, name='form_insert_personnel'),  #miditra amn insertion ana personnel
    path('save_personnel',save_personnel, name='save_personnel'), #save les personnels
    path('liste_personnel',liste_personnel, name='liste_personnel'), #lister les personnels
    path('personnel/<int:idPersonnel>',delete_personnel, name='delete_personnel'), #supprimer les personnels
    path('personnel/<int:idPersonnel>/modifier',modify_personnel, name='modify_personnel'), #modifier personnel
    path('personnel/<int:idPersonnel>/detail',detail_personnel, name='detail_personnel'),#detailler personnel modifée
    path('save_login',save_login, name='save_login'), #sauvegarder le compte du personnel




]
