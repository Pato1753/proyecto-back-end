from django import forms

class BaseUsernameForm(forms.ModelForm):
    user_name = forms.CharField(
        label= "Username",
        widget=forms.TextInput(attrs={
            "class": "form form__input",
            "placeholder": "@username"
            }))