from ..models import MetricasH
from .formBase.BaseNombreMetricasHForm import BaseNombreMetricasHForm
from .formBase.BasePlataformaForm import BasePlataformaForm
from .formBase.BaseFechaAnalisisForm import BaseFechaAnalisisForm
from .formBase.BaseVideoForm import BaseVideoForm
from .formBase.BaseSeguidoresForm import BaseSeguidoresForm
from .formBase.BaseLikeForm import BaseLikeForm
from .formBase.BaseComentariosForm import BaseComentariosForm
from .formBase.BaseVistasForm import BaseVistasForm


class CrearMetricasForm(BaseNombreMetricasHForm,
                          BasePlataformaForm,
                          BaseFechaAnalisisForm,
                          BaseVideoForm,
                          BaseSeguidoresForm,
                          BaseLikeForm,
                          BaseComentariosForm,
                          BaseVistasForm):
    class Meta:
        model = MetricasH
        fields = ["nombre_metrica",
                  "plataforma",
                  "video",
                  "fecha_analisis",
                  "vistas",
                  "seguidores",
                  "vistas",
                  "likes",
                  "comentarios"
                  ]