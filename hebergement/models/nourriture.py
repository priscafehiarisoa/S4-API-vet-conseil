from django.db import models


class Nourriture(models.Model):
    designation = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    prix_par_unite = models.FloatField()
    unite = models.FloatField()

    def __str__(self):
        return self.designation