from django import forms

class BaseLikeForm(forms.ModelForm):
    likes = forms.IntegerField(
        label= "Likes",
        widget=forms.NumberInput(attrs={
            "class": "form form__input",
            "placeholder": "Cantidad de likes"
            }))