from django.db import models
from django.core.validators import MaxValueValidator

class Poste(models.Model):
    designation = models.CharField(max_length=255)
    rang = models.IntegerField(validators=[MaxValueValidator(10)], default=2)
    
