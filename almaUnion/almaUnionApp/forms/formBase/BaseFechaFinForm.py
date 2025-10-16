from django import forms

class BaseFechaFinForm(forms.ModelForm):
    fecha_fin = forms.DateTimeField(
        label= "Fecha de Cierre",
        widget=forms.DateTimeInput(attrs={
            "class": "form form_input",
            "placeholder": "18/11"
            }))