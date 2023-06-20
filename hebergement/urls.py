from django.urls import include, path

from hebergement.views import test

urlpatterns = [
    path("", test.index, name="index"),

]