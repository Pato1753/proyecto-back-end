from django import forms

class BaseSeguidoresForm(forms.ModelForm):
    seguidores = forms.IntegerField(
        label= "Cantidad de seguidores",
        widget=forms.NumberInput(attrs={
            "class": "form form__input",
            "placeholder": "Ingrese cantidad de seguidores del canal"
            }))
    
    def clean_seguidores(self):
        seguidores = self.cleaned_data.get('seguidores')
        if seguidores is not None and seguidores < 100:
            # Ejemplo de validación personalizada: mínimo de seguidores
            raise forms.ValidationError("El influencer debe tener al menos 100 seguidores para actualizar su perfil.")
        return seguidores