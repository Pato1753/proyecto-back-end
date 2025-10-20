
from ..models import Usuarios
from .formBase.BaseEmailForm import BaseEmailForm
from .formBase.BaseContrasenaForm import BaseContrasenaForm
    
class InicioForm( BaseEmailForm, BaseContrasenaForm):
    class Meta():
        model = Usuarios
        fields = ["email",
                  "contrasena"]
        
    def validate_unique(self):  # evita que el UNIQUE del modelo invalide el login
        pass

    def save(self, *args, **kwargs):  # nunca se debe guardar en login
        raise NotImplementedError("InicioForm no guarda en BD (solo autentica).")