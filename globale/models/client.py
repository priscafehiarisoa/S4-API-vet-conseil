from django.db import models

class Client(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    facebook=models.CharField(max_length=255)

    def __str__(self):
        return self.nom


    def get_animaux(self):
        liste_animaux=Patient.objects.filter(proprietaire=this.id)
        return liste_animaux