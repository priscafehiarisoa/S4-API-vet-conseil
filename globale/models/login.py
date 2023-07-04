from django.db import models

from . import Personnel

class Login(models.Model):
    mail=models.CharField(max_length=255)
    mot_de_passe=models.CharField(max_length=255)
    personnel=models.ForeignKey(Personnel, on_delete=models.CASCADE)