from django import forms

class BaseNombreEmpresaForm(forms.ModelForm):
    nombre_empresa = forms.CharField(
        label= "Nombre de la empresa",
        widget=forms.TextInput(attrs={
            "class": "form form__input",
            "placeholder": "Ej: TermoSupreme"
            }))