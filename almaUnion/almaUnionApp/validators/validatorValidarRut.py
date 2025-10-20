from django.utils.translation import gettext_lazy
from django.core.exceptions import ValidationError

def validar_rut(value):
    if not value.isalnum() or len(value) < 5 or len(value) > 45:
        raise ValidationError(
            gettext_lazy('%(value)s no es un RUT válido. Debe contener solo números y/o letras y tener entre 5 y 45 caracteres.'),
            params={'value': value},
        )