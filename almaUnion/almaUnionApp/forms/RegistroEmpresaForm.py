# Modelos utilizados
from ..models import Usuarios, Empresas, RedesSociales
# Base de Usuarios
from .formBase.BaseEmailForm import BaseEmailForm
from .formBase.BaseContrasenaForm import BaseContrasenaForm
# Base de Influencer
from .formBase.BaseRutEmpresaForm import BaseRutEmpresaForm
from .formBase.BaseNombreEmpresaForm import BaseNombreEmpresaForm
from .formBase.BaseCategoriaEmpresaForm import BaseCategoriaEmpresaForm
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
            "contrasena",
            ]

class RegistroEmpresaForm( BaseRutEmpresaForm, BaseNombreEmpresaForm, BaseCategoriaEmpresaForm):
    class Meta:
        model = Empresas
        fields = [
            "rut_empresa",
            "nombre_empresa",
            "categoria_empresa",   
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