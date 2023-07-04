from django.db import models

from globale.models import Race
from hebergement.models.nourriture import Nourriture


class Attribution(models.Model):
    nourriture=models.ForeignKey(Nourriture,on_delete=models.CASCADE)
    race=models.ForeignKey(Race,on_delete=models.CASCADE)
    debut_interval_poids=models.IntegerField()
    fin_interval_poids=models.IntegerField()

    @staticmethod
    def check_if_available(race_id,nourriture):
        liste_attributions=Attribution.objects.filter(race_id=race_id,nourriture=nourriture)
        for i in liste_attributions:
            if i.race_id==race_id and nourriture==i.nourriture:
                return True
        return False