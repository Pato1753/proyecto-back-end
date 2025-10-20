from django import forms
from ..models import Campanas
from .formBase.BaseNombreCampanaForm import BaseNombreCampanaForm
from .formBase.BaseDescripcionForm import BaseDescripcionForm
from .formBase.BasePresupuestoForm import BasePresupuestoForm
from .formBase.BaseFechaInicioForm import BaseFechaInicioForm
from .formBase.BaseFechaFinForm import BaseFechaFinForm

class CrearCampanasForm( BaseNombreCampanaForm,
                        BaseDescripcionForm,
                        BasePresupuestoForm,
                        BaseFechaInicioForm,
                        BaseFechaFinForm):
    class Meta:
        model = Campanas
        fields = ["nombre_campana",
                  "descripcion",
                  "presupuesto",
                  "fecha_inicio",
                  "fecha_fin"
                  ]