from django.urls import path
from frontVetConseil.views import user_area_view

urlpatterns = [
    path("", user_area_view.index, name="index"),
]