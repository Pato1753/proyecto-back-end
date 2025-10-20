from django import forms

class BaseNombreCampanaForm(forms.ModelForm):
    nombre_campana = forms.CharField(
        label= "Nombre de la Campañia",
        widget=forms.TextInput(attrs={
            "class": "form form__input",
            "placeholder": "Ingrese una campaña"
            }))