from django import forms
from ...choices.CategoriasChoices import CategoriasChoise

class BaseCategoriaEmpresaForm(forms.ModelForm):
    categoria_empresa = forms.ChoiceField(
        label="Categoria de la Empresa",
        choices=CategoriasChoise.choices,
        widget=forms.Select(attrs={
            "class": "form form__select",
            "placeholder": "Ingrese la categoria"
            }))