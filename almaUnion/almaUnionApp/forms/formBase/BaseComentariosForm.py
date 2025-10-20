from django import forms

class BaseComentariosForm(forms.ModelForm):
    comentarios = forms.IntegerField(
        label= "Comentarios",
        widget=forms.NumberInput(attrs={
            "class": "form form__input",
            "placeholder": "Cantidad de comentarios"
            }))