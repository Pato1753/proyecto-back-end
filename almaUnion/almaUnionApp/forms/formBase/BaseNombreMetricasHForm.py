from ...models import MetricasH

from django import forms

class BaseNombreMetricasHForm(forms.ModelForm):
    nombre_metrica = forms.CharField(
        label= "Nombre de la Metrica",
        widget=forms.TextInput(attrs={
            "class": "form form__input",
            "placeholder": "Ingrese nombre de la Metrica"
            }))