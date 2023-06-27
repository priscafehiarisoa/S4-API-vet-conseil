from django.db import models

from hebergement.models.client import Client
from hebergement.models.race import Race


class Patient(models.Model):
    nature = models.ForeignKey(Race, on_delete=models.CASCADE)
    age = models.IntegerField()
    proprietaire = models.ForeignKey(Client, on_delete=models.CASCADE)
    nom = models.CharField(max_length=30, default="")

    def __str__(self):
        res = self.nom+" | "+ self.nature.designation
        return res
