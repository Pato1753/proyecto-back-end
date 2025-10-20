from django import forms

class BasePresupuestoForm(forms.ModelForm):
    presupuesto = forms.DecimalField(
        label= "Presupuesto",
        widget=forms.NumberInput(attrs={
        "class": "form form_input",
        "placeholder": "12345"
    }))