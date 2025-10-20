# almaUnionApp / choices / rolchoices.py

from django.db import models

class RolChoices(models.TextChoices):
    INFLUENCER = "influencer", "Influencer"
    EMPRESA = "empresa", "Empresa"