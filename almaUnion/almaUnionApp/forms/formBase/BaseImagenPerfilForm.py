from django import forms

class BaseImagenPerfilForm(forms.ModelForm):
    imagen_perfil = forms.ImageField(
        label="Imagen",
        widget=forms.ClearableFileInput(attrs={
            "class": "form form_file",
            "placeholder":  "Ingrese una imagen",
            "accept": ".pdf, .jpg. png."
            }))