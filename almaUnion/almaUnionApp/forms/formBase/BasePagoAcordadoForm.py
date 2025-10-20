from django import forms

class BasePagoAcordadoForm(forms.ModelForm):
    pago_acordado = forms.DecimalField(
        label= "Pago Acordado",
        widget=forms.NumberInput(attrs={
            "class": "form form__input",
            "placeholder": "1.235.413"
            }))