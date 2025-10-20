from django import forms

class BaseDescripcionForm(forms.ModelForm):
    descripcion = forms.CharField(
        label= "Descripción",
        widget=forms.Textarea(attrs={
            "class": "form form_textarea",
            "placeholder": "Descripcion"
        }))