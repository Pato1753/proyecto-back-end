from django import forms
from ...choices.CategoriasChoices import CategoriasChoise

class BaseCategoriaInfluencerForm(forms.ModelForm):
    categoria_influencer = forms.ChoiceField(
        label= "Categoria Influencer",
        choices=CategoriasChoise.choices,
        widget=forms.Select(attrs={
            "class": "form form__input",
            "placeholder": "Ingrese la categoria"
            }))