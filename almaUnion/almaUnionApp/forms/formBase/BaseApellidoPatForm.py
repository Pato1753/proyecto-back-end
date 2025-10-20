from django import forms

class BaseApellidoPatForm(forms.ModelForm):
    apellido_pat = forms.CharField(
        label="Apellido Paterno",
        widget=forms.TextInput(attrs={
            "class": "form form__input",
            "placeholder": "Ingrese su apellido paterno"
            }))