from django.urls import path
from frontVetConseil.views import user_area_view

urlpatterns = [
    path("", user_area_view.index, name="index"),
    path("login", user_area_view.login, name="login"),
    path("authentification", user_area_view.authentification, name="authentification"),
    path("inscription", user_area_view.inscription, name="inscription"),
    path("save", user_area_view.save, name="save"),
]