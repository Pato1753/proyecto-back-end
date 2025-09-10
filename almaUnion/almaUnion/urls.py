"""
URL configuration for almaUnion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from almaUnionApp.views import (renderTemplateMenuInicial, renderTemplateRegistroEmpresa,
                                renderTemplateRegistroInfluencer,renderTemplatesLogin , renderTemplateHubEmpresa,
                                renderTemplateHubInfluencer, renderTemplateCampanias,
                                renderTemplateConfiguracion, renderTemplateInfluencers,
                                renderTemplateInformes, renderTemplateMensajes,
                                renderTemplatePagos, renderTemplateOportunidades,
                                renderTemplatePerfil)
urlpatterns = [
    # Agrupación path admin 
    path('admin/', admin.site.urls),
    # Agrupación path Menu inicial
    path("", renderTemplateMenuInicial, name='inicio'),
    # Agrupación path Registro de usuario
    path("registroEmpresa/",renderTemplateRegistroEmpresa, name='registroEmpresa'),
    path("registroInfluencer/", renderTemplateRegistroInfluencer, name='registroInfluencer'),
    path("Login-Influencer/", renderTemplatesLogin, name='Login'),
    # Agrupación path redirección al Hub
    path("hubEmpresa/", renderTemplateHubEmpresa, name='hubEmpresa'),
    path("hubInfluencer/", renderTemplateHubInfluencer, name='hubInfluencer'),
    # agrupación path redirección aside común influencer-Empresa
    path("perfil/", renderTemplatePerfil, name='perfil'), 
    path("configuracion/", renderTemplateConfiguracion, name='configuracion'),
    # Agrupación path redirección aside Empresa
    path("influencers/", renderTemplateInfluencers, name='influencers' ),
    path("campanias/", renderTemplateCampanias, name='campanias'),
    path("mensajes/", renderTemplateMensajes, name='mensajes'),
    path("pagos/", renderTemplatePagos, name='pagos'),
    # Agrupación path redirección aside influencers
    path("oportunidades/", renderTemplateOportunidades, name='oportunidades'),
    path("informes/", renderTemplateInformes, name='informes'),
]
