from django import forms
from ...validators.validatorValidarRut import validar_rut

class BaseRutInfluencerForm(forms.ModelForm):
    rut_influencer = forms.CharField(
        label= "Rut del Influencer",
        validators=[validar_rut,],
        error_messages={
            'unique': "Este Rut ya está registrado por otro .",
            'max_length': "El RUT no puede exceder los 45 caracteres."
            },
        widget=forms.TextInput(attrs={
            "class": "form form__input",
            "placeholder": "Ingrese su rut"
            }))