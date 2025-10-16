from django.db import models

class PlataformaChoise(models.TextChoices):
    # Variable = Lo que guarda la db, Muestra al usuario
    INSTAGRAM = "instagram", "Instagram"
    TIKTOK = "tiktok", "TikTok"
    YOUTUBE = "youtube", "YouTube"
    FACEBOOK = "facebook", "Facebook"
    X = "x", "X/ Twitter"