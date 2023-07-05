from datetime import datetime, timedelta, time

from django.db import models
from pytz import utc
from globale.models import Patient, Personnel
from django.utils import timezone
from django.db.models import Q

from django.core.exceptions import ValidationError

from django.db.models.functions import ExtractMonth
from django.db.models import Count
#from vet.models import v_patient

def validate_positive_integer(value):
    if value <= 0:
        raise ValidationError("La valeur doit être un entier positif.")

def validate_positive_float(value):
    if value <= 0:
        raise ValidationError("La valeur doit être un nombre à virgule positive.")

class Rendez_vous(models.Model):
    date_de_prise = models.DateTimeField(default=timezone.now)
    date_fin = models.DateTimeField(default=timezone.now)
    date_consultation = models.DateTimeField(default=timezone.now)
    duree = models.IntegerField(default=1, validators=[validate_positive_integer])
    raison = models.CharField(max_length=700)
    temps = models.IntegerField(default=0, validators=[validate_positive_integer])
    prix = models.FloatField(validators=[validate_positive_float])
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    etat = models.IntegerField(default=0, validators=[validate_positive_integer])

    def clean(self):
        if self.raison == "":
            raise ValidationError("Raison vide")
        
        if int(self.duree)   <= 0:
            raise ValidationError("La durée doit-être strictement positive")

        if self.date_consultation >= self.date_de_prise:
            raise ValidationError("La date de consultation doit être antérieure à la date de prise.")
        
        if self.date_de_prise >= self.date_fin:
            raise ValidationError("La date de prise doit être antérieure à la date de fin.")

    def save(self, *args, **kwargs):
        self.clean()
        super(Rendez_vous, self).save(*args, **kwargs)

    def recherche_date_libre(self, date_debut, date_fin):
        date_occupées = Rendez_vous.objects.filter(
            date_de_prise__range=(date_debut, date_fin), etat = 0
        )
        return date_occupées
    
    def dates_libres(self, date_debut, date_fin):
        
        date_occupées = self.recherche_date_libre(date_debut, date_fin)
        donnees_de_test = date_occupées
        dates_libres = []
        
        for i in range(len(donnees_de_test)):
            if donnees_de_test[i].date_de_prise > date_debut:
                constant_date = {
                    'date_de_prise': date_debut,
                    'date_fin': donnees_de_test[i].date_de_prise,
                }
                dates_libres.append(constant_date)
            date_debut = donnees_de_test[i].date_fin
        derniere_date = {
            'date_de_prise': date_debut,
            'date_fin': date_fin,
        }

        if(len(date_occupées) > 0):
            derniere_date = {
                'date_de_prise': date_occupées[len(date_occupées) - 1].date_fin,
                'date_fin': date_fin,
            }

        dates_libres.append(derniere_date)
        return dates_libres

    def rendez_vous_à_supprimer(self, id_rendez_vous):
        rendez_vous = Rendez_vous.objects.get(id=id_rendez_vous)
        return rendez_vous

    def rendez_vous_entre_dates(self, date_debut, date_fin):
        rendez_vous = Rendez_vous.objects.filter(date_de_prise__range=(date_debut, date_fin), etat = 0)
        return rendez_vous    

    def get_all_rendezvous(self):
        return Rendez_vous.objects.filter(etat = 0)
    
    def get_all_rendez_vous_by_date(self, date):
        return Rendez_vous.objects.filter(date_de_prise__date=date, etat = 0)

    def rendez_vous_entre_2_dates(self, date_debut, date_fin):
        return Rendez_vous.objects.filter(date_de_prise__range=(date_debut, date_fin), etat = 0)

    def check_date(self):

        all_rendezvous_dates = Rendez_vous.objects.filter(
            Q(date_de_prise__range=(self.date_de_prise, self.date_fin)) |
            Q(date_fin__range=(self.date_de_prise, self.date_fin)),
            Q(etat = 0)
        )

        if all_rendezvous_dates.exists():
            raise ValidationError("Date déjà occupée")
        self.save()

    def check_demande(self):
        all_rendezvous_dates = Rendez_vous.objects.filter(
            Q(date_de_prise__range=(self.date_de_prise, self.date_fin)) |
            Q(date_fin__range=(self.date_de_prise, self.date_fin)),
            Q(etat = 2)
        )

        if all_rendezvous_dates.exists():
            raise ValidationError("Date déjà occupée")
        self.save()
    def files_for_new_date(self):
        rendez_vous_par_mois = Rendez_vous.objects.annotate(mois=ExtractMonth('date_de_prise')).values('mois').annotate(count=Count('id')).order_by('mois')
        labels = []
        valeurs = []
        mois_nom = {"1":"Janvier", "2":"Feb", "3":"Mar", "4":"Apr", "5":"May", "6":"Jun", "7":"Jul", "8":"Aug", "9":"Sep", "10":"Oct","11":"Nov", "12":"Dec"}
        for rendez_vous in rendez_vous_par_mois:
            mois = rendez_vous['mois']
            count = rendez_vous['count']
            labels.append(mois_nom[str(mois)])
            valeurs.append(count)
        patients = Patient.objects.all()
        context = {
            'labels': labels,
            'valeurs': valeurs,
            'patients' : patients
        }
        return context
    
    def obtenir_demande_rendez_vous(self): # 2 etat demaned
        rendez_vous = Rendez_vous.objects.filter(etat = 2)
        return rendez_vous
    
    def update_time_out_rendez_vous(self):
        rendez_vous = Rendez_vous.objects.filter(etat = 0)
        for rendez_vou in rendez_vous:
            if rendez_vou.date_de_prise < timezone.now():
                rendez_vou.etat = 1
                rendez_vou.save()