from django import forms

class BaseRutInfluencerForm(forms.ModelForm):
    rut_influencer = forms.CharField(
        label= "Rut del Influencer",
        widget=forms.TextInput(attrs={
            "class": "form form__input",
            "placeholder": "Ingrese su rut"
            }))