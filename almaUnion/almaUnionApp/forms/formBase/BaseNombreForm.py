from django import forms

class BaseNombreForm(forms.ModelForm):
    nombre = forms.CharField(
        label= "Nombre del influencer",
        widget=forms.TextInput(attrs={
            "class": "form form__input",
            "placeholder": "Ingrese su nombre"
            }))
    
    # Validación adicional para garantizar que el nombre no sea 'admin' 
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if nombre and nombre.lower() == 'admin':
            raise forms.ValidationError("El nombre 'Admin' no está permitido.")
        return nombre