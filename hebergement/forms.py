from django import forms

from hebergement.models import  Nourriture
from globale.models import Client, Patient


class Date_validation_form(forms.Form):
    date_debut = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}),
        input_formats=['%Y-%m-%d']
    )
    date_fin = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}),
        input_formats=['%Y-%m-%d']
    )


class Ajouter_hebergement_form(forms.Form):
    client = forms.ModelChoiceField(queryset=Client.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
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


class Modifier_tarif_form(forms.Form):
    id_race = forms.IntegerField(widget=forms.TextInput({'class': 'form-control', 'type': 'number'}), required=False)
    id_tarif = forms.IntegerField(widget=forms.TextInput({'class': 'form-control', 'type': 'number'}), required=False)
    race = forms.CharField(widget=forms.TextInput({'class': 'form-control', 'disabled': 'True'}), required=False)
    montant_journalier = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0,
                                            widget=forms.TextInput({'class': 'form-control', 'type': 'number'}))
    montant_horaire = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0,
                                         widget=forms.TextInput({'class': 'form-control', 'type': 'number'}))
