from django.db import models

class EstadosChoices(models.TextChoices):
    PROPUESTA = "propuesta", "Propuesta"
    ACEPTADA = "aceptada", "Aceptada"
    ENPROCESO = "en proceso", "En Proceso"
    FINALIZADO = "finalizado", "Finalizado"