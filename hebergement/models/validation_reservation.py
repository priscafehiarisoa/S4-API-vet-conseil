from django.db import models

from hebergement.models import Reservation


class Validation_reservation(models.Model):
    date_validation=models.DateTimeField(auto_now_add=True)
    reservation=models.ForeignKey(Reservation,on_delete=models.CASCADE)