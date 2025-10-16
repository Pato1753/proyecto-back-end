from django import forms

class BaseCanalForm(forms.ModelForm):
    canal = forms.URLField(
        label="Canal",
        widget=forms.URLInput(attrs={
            "class": "form form__input",
            "placeholder": "https://"
            }))