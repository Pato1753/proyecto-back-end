from django import forms

class BaseFechaAnalisisForm(forms.ModelForm):
    fecha_analisis = forms.DateTimeField(
        label= "Fecha de analisis",
        widget=forms.DateTimeInput(attrs={
            "class": "form form__input"
            }))