from django import forms
from ...choices.PlataformaChoices import PlataformaChoise

class BasePlataformaForm(forms.ModelForm):
    plataforma = forms.ChoiceField(
        label= "Plataforma",
        choices=PlataformaChoise.choices,
        widget=forms.Select(attrs={
            "class": "form form__select"
            }))