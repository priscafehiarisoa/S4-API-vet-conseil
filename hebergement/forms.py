from django import forms

class Date_validation_form(forms.Form):
    date_debut = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date','class': 'form-control'}),
        input_formats = ['%Y-%m-%d']
    )
    date_fin = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date','class': 'form-control'}),
        input_formats=['%Y-%m-%d']
    )
