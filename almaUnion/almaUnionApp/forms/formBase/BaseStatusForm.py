from django import forms

class BaseStatusForm(forms.ModelForm):
    status = forms.ChoiceField(
        label= "Estado",
        widget=forms.Select(attrs={
        "class": "form form__select",
    }))