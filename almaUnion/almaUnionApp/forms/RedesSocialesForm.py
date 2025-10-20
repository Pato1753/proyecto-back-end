
from django import forms
from ..models import RedesSociales
from .formBase.BasePlataformaForm import BasePlataformaForm
from .formBase.BaseUsernameForm import BaseUsernameForm
from .formBase.BaseCanalForm import BaseCanalForm
from .formBase.BaseSeguidoresForm import BaseSeguidoresForm
from .formBase.BaseVistasForm import BaseVistasForm

class RedesSocialesForm( BasePlataformaForm, BaseUsernameForm, BaseCanalForm, BaseSeguidoresForm, BaseVistasForm):
    class Meta:
        model = RedesSociales
        fields = [
            "plataforma",
            "user_name",
            "canal",
            "seguidores",
            "vistas"
        ]