from django import forms
# Asegúrate de importar CategoriasChoise desde la ubicación correcta
from almaUnionApp.choices.CategoriasChoices import CategoriasChoise 

class OportunidadesFiltroForm(forms.Form):
    # Campo de selección para categorías
    categoria = forms.ChoiceField(
        # Añade una opción vacía ("") con el texto "Todas" al inicio de las opciones
        choices=[('', 'Todas')] + list(CategoriasChoise.choices),
        required=False,
        # Agregamos la clase 'filter-form-select' si queremos un estilo específico, 
        # pero usaremos las clases genéricas de CSS para simplificar.
    )
    
    # Campo para presupuesto mínimo
    presupuesto_min = forms.IntegerField(
        required=False,
        min_value=0,
        label="Presupuesto mínimo",
        # Agregamos el widget para aplicar las clases CSS y el placeholder
        widget=forms.NumberInput(attrs={
            'placeholder': 'Min. Presupuesto',
            'class': 'budget-input' # Usamos una clase que ya está estilizada
        })
    )