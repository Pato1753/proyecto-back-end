from django import forms

class BaseEmailForm(forms.ModelForm):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            "class": "form form_input",
            "placeholder": "user@gmail.com",
            }))
    
    def clean_email(self):
        return self.cleaned_data["email"].strip().lower()