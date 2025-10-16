from django import forms
# Modelos
from ..models import Usuarios, Influencers, RedesSociales
from  django.contrib.auth.hashers import make_password
# Base de Usuarios
from .formBase.BaseEmailForm import BaseEmailForm
from .formBase.BaseContrasenaForm import BaseContrasenaForm
# Base de Influencer
from .formBase.BaseRutInfluencerForm import BaseRutInfluencerForm
from .formBase.BaseCategoriaInfluencerForm import BaseCategoriaInfluencerForm
from .formBase.BaseNombreForm import BaseNombreForm
from .formBase.BaseApellidoPatForm import BaseApellidoPatForm
from .formBase.BaseApellidoMatForm import BaseApellidoMatForm
from .formBase.BasePromViewsForm import BasePromViewsForm
# Base de Redes Sociales
from .formBase.BasePlataformaForm import BasePlataformaForm
from .formBase.BaseUsernameForm import BaseUsernameForm
from .formBase.BaseCanalForm import BaseCanalForm
from .formBase.BaseSeguidoresForm import BaseSeguidoresForm
from .formBase.BaseVistasForm import BaseVistasForm

class RegistroUsuarioForm( BaseEmailForm, BaseContrasenaForm):
    
    class Meta:
        model = Usuarios
        fields = [
            "email",
            "contrasena"
            ]
        
    def clean_email(self):
        email = super().clean_email() if hasattr(super(), "clean_email") else self.cleaned_data["email"].strip().lower()
        if Usuarios.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Ya existe una cuenta con este correo.")
        return email

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.email = usuario.email.lower()
        usuario.contrasena = make_password(self.cleaned_data["contrasena"])
        if commit:
            usuario.save()
        return usuario
        
        

class RegistroInfluencerForm( BaseRutInfluencerForm, BaseCategoriaInfluencerForm, BaseNombreForm, BaseApellidoPatForm, BaseApellidoMatForm, BasePromViewsForm):
    class Meta:
        model = Influencers
        fields = [
            "rut_influencer",
            "nombre",
            "categoria_influencer",
            "apellido_pat",
            "apellido_mat",
            "prom_views",
        ]

class RegistroRedesSocialesForm( BasePlataformaForm, BaseUsernameForm, BaseCanalForm, BaseSeguidoresForm, BaseVistasForm):
    class Meta:
        model = RedesSociales
        fields = [
            "plataforma",
            "user_name",
            "canal",
            "seguidores",
            "vistas",
            ]
        


