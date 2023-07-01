from django.db import models

from globale.models import Race


class Tarifs_Hebergement(models.Model):
    race=models.ForeignKey(Race,on_delete=models.CASCADE)
    date_changement_tarif=models.DateField()
    montant_journalier=models.DecimalField(max_digits=10,decimal_places=2)
    montant_horaire=models.DecimalField(max_digits=10,decimal_places=2)
