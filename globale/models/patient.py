from django.db import models

from . import Client
from . import Race


class Patient(models.Model):
    nature=models.ForeignKey(Race, on_delete=models.CASCADE)
    age=models.IntegerField()
    proprietaire=models.ForeignKey(Client, on_delete=models.CASCADE)