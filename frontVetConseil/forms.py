from django import forms

from hebergement.models import  Nourriture
from globale.models import Client, Patient

class Ajouter_hebergement_user_form(forms.Form):
    animal = forms.ModelChoiceField(queryset=Patient.objects.all(),
                                    widget=forms.Select(attrs={'class': 'form-control'}))
    date_debut_hebergement = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
                                             input_formats=['%Y-%m-%d'])
    date_fin_hebergement = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
                                           input_formats=['%Y-%m-%d'])
    type_nourriture = forms.ModelChoiceField(queryset=Nourriture.objects.all(),
                                             widget=forms.Select(attrs={'class': 'form-control'}))
    quantite = forms.FloatField(min_value=0,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'veuillez entrer la quantité à administrer par ration'}))
    frequence_nourriture = forms.IntegerField(min_value=0, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'ex:2'}))
    medicaments = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'custom-control-input', 'type': 'checkbox', 'id': 'customSwitch1'}))

    tarif_journalier = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'custom-control-input', 'type': 'checkbox', 'id': 'customSwitch2'}))
    frequence_medicament = forms.IntegerField(min_value=0, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'fréquence du/des medicaments , ex: 3'}))
    def __init__(self, proprietaire_instance, *args, **kwargs):
        super(Ajouter_hebergement_user_form, self).__init__(*args, **kwargs)
        self.fields['animal'] = forms.ModelChoiceField(
            queryset=Patient.objects.filter(proprietaire=proprietaire_instance),
            widget=forms.Select(attrs={'class': 'form-control'})
        )
  