from django import forms

class BaseVistasForm(forms.ModelForm):
    vistas = forms.IntegerField(
        label="Cantidad de vistas",
        widget=forms.NumberInput(attrs={
            "class": "form form__input",
            "placeholder": "Ingrese cantidad de vistas totales"
            }))