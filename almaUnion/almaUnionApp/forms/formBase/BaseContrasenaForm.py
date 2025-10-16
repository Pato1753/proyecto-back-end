from django import forms

class BaseContrasenaForm(forms.ModelForm):
    contrasena = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            "class": "form form__input",
            "placeholder": "Ingresa una contraseña",
            "autocomplete": "current-password",
        })
    )