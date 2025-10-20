from django import forms

class BasePromViewsForm(forms.ModelForm):
    prom_views = forms.FloatField(
        label= "Vistas Promedio",
        widget=forms.NumberInput(attrs={
            "class": "form form__input",
            "placeholder": "Ingrese sus vistas promedio",
            }))