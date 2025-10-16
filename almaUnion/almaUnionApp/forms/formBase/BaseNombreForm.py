from django import forms

class BaseNombreForm(forms.ModelForm):
    nombre = forms.CharField(
        label= "Nombre del influencer",
        widget=forms.TextInput(attrs={
            "class": "form form__input",
            "placeholder": "Ingrese su nombre"
            }))