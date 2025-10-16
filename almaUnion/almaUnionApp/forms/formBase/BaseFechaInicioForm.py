from django import forms

class BaseFechaInicioForm(forms.ModelForm):
    fecha_inicio = forms.DateTimeField(
        label= "Fecha de inicio",
        widget=forms.DateTimeInput(attrs={
            "class": "form form_input",
            "placeholder": "18/11"
            }))