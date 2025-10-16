from django.db import models

class CategoriasChoise(models.TextChoices):
    TECNOLOGIA = "tecnologia", "Tecnología"
    TURISMO = "turismo", "Turismo"
    EDUCACION = "educacion", "Educación"
    SALUD = "salud", "Salud"