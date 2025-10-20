from django import forms

class BaseRutEmpresaForm(forms.ModelForm):
    rut_empresa = forms.CharField(
        label= "Rut de empresa",
        widget=forms.TextInput(attrs={
            "class": "form form__input",
            "placeholder": "Ingrese el rut de la empresa"
            }))
