from django.db import models
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.core.exceptions import ValidationError

class Client(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    facebook=models.CharField(max_length=255)
    password=models.CharField(max_length=255)

    def checkClient(self):
        if self.nom == '':
            raise ValidationError("Le nom est requis")
        if self.prenom == '':
            raise ValidationError("Le prenom est requis")
        if self.adresse == '':
            raise ValidationError("email requis")
        if self.contact == '':
            raise ValidationError("contact requis")
        if self.facebook == '':
            raise ValidationError("Facebook account exiged")
        if self.password == '':
            raise ValidationError("Password not set")

    def __str__(self):
        return self.nom

    def get_animaux(self):
        liste_animaux=Patient.objects.filter(proprietaire=this.id)
        return liste_animaux

    def authentification(self):
        try:
            client = get_object_or_404(Client, mail=self.mail, password=self.password)
            return client
        except Http404:
            return None

    def jsonClient(self):
        json_data = {
            "id": self.id,
            "nom": self.nom,
            "prenom": self.prenom,
            "adresse": self.adresse,
            "mail": self.mail,
            "contact": self.contact,
            "facebook": self.facebook,
            "password": self.password
        }
        return json_data