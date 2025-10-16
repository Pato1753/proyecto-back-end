from django import forms

class BaseSeguidoresForm(forms.ModelForm):
    seguidores = forms.IntegerField(
        label= "Cantidad de seguidores",
        widget=forms.NumberInput(attrs={
            "class": "form form__input",
            "placeholder": "Ingrese cantidad de seguidores del canal"
            }))