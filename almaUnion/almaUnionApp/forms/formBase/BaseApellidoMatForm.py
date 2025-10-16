from django import forms
# from ...validators.validatorPrueba import validar_par

class BaseApellidoMatForm(forms.ModelForm):
    apellido_mat = forms.CharField(
        label="Apellido Materno",
        # Validar_par es un ejemplo para saber donde se coloca los validatos
        validators=[
            #validar_par(),
            ],
        widget=forms.TextInput(attrs={
            "class": "form form__input",
            "placeholder": "Ingrese su apellido materno"
            }))
