from django import forms
from globale.models import Poste
from globale.models import Personnel

class PosteForm(forms.ModelForm):
    class Meta:
        model = Poste
        fields = ['designation','rang']

class PersonnelForm(forms.ModelForm):
    class Meta:
        model = Personnel
        fields = ['nom','prenom','adresse','contact','poste']
