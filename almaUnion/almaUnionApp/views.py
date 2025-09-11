from django.shortcuts import render
from datetime import datetime

# Create your views here.
def renderTemplateMenuInicial(request):
    return render(request, "templatesApp/templateMenuInicial.html")

def renderTemplateRegistroEmpresa(request):
    return render(request, "templatesApp/templateRegistroEmpresa.html")

def renderTemplateRegistroInfluencer(request):
    return render(request, "templatesApp/templateRegistroInfluencer.html")

def renderTemplateHubEmpresa(request):
    # Para cambiar el nombre de la empresa
    infoPerfil = {"fotoPerfil": "assets/avatarEmpresa.png", "nombrePerfil": "Patricio Patoso"}
    botones = [
        {"label": "Inicio", "viewName": "inicio", "sourceImagen":"assets/casa.png", "sourceAlternative": "inicioLogo"},
        {"label": "Influencers", "viewName": "influencers", "sourceImagen":"assets/users.png", "sourceAlternative": "influencersLogo" },
        {"label": "Campañas", "viewName": "campanias", "sourceImagen":"assets/metricas.png", "sourceAlternative": "campañaLogo" },
        {"label": "Perfil", "viewName": "perfil", "sourceImagen":"assets/user.png", "sourceAlternative": "userLogo" },
        {"label": "Mensajes", "viewName": "mensajes", "sourceImagen":"assets/burbuja.png", "sourceAlternative": "mensajeLogo" },
        {"label": "Pagos", "viewName": "pagos", "sourceImagen":"assets/tarjetaDeBanco.png", "sourceAlternative": "pagosLogo" },
        {"label": "Configuración", "viewName": "configuracion", "sourceImagen":"assets/ajustes.png", "sourceAlternative": "configuraciónLogo" },
    ]
    return render(request, "templatesApp/templateHubEmpresa.html", {"botones" : botones, "infoPerfil": infoPerfil})
  
def renderTemplateHubInfluencer(request):    
    infoPerfil = {"fotoPerfil": "assets/avatarInfluencer.png", "nombrePerfil": "Rubí Rubíes"}
    
    botones = [
        {"label": "Inicio", "viewName": "inicio", "sourceImagen": "assets/casa.png", "sourceAlternative": "inicioLogo"},
        {"label": "Oportunidades", "viewName": "oportunidades", "sourceImagen": "assets/maleta.png", "sourceAlternative": "oportunidadesLogo"},
        {"label": "Informes", "viewName": "informes", "sourceImagen": "assets/metricas.png", "sourceAlternative": "informesLogo"},
        {"label": "Perfil", "viewName": "perfil", "sourceImagen": "assets/user.png", "sourceAlternative": "perfilLogo"},
        {"label": "Configuración", "viewName": "configuracion", "sourceImagen": "assets/ajustes.png", "sourceAlternative": "configuraciónLogo"},
    ]
    contexto = {
        "botones": botones,
        "infoPerfil": infoPerfil
    }
    
    return render(request, "templatesApp/templateHubInfluencer.html", contexto)


# Render en común influencer-Empresa
def renderTemplateConfiguracion(request):
    return render(request, "templatesApp/templateConfiguracion.html")

def renderTemplatePerfil(request):
    return render(request, "templatesApp/templatePerfil.html")

# Render para influencer
def renderTemplateOportunidades(request):
    return render(request, "templatesApp/templateOportunidades.html")

def renderTemplateInformes(request):
    return render(request, "templatesApp/templateInformes.html")

# Render para Empresa
def renderTemplateInfluencers(request):
    return render(request, "templatesApp/templateInfluencers.html")

def renderTemplateCampanias(request):
    campanias=[{"nombre" : "Viltrum puede","presupuesto": 10000000, "descripcion": "Vamos a ayudar a la tierra y tu serás nuestro mensajero", "fechaInicio": datetime.fromisoformat("2026-09-11"),"fechaFin":datetime.fromisoformat("2026-09-12")}]
    return render(request, "templatesApp/templateCampanias.html", {"campanias": campanias})

def renderTemplateMensajes(request):
    return render(request, "templatesApp/templateMensajes.html")

def renderTemplatePagos(request):
    return render(request, "templatesApp/templatePagos.html")

# render para campanias
def renderTemplatex(request):
    return render(request, "templatesApp/templatex.html")

def renderTemplateCrearCampanias(request):
    return render(request, "templatesApp/templateCrearCampania.html")

def renderTemplateModificarCampanias(request):
    campanias = {"nombre" : "Viltrum puede","presupuesto": 10000000, "descripcion": "Vamos a ayudar a la tierra y tu serás nuestro mensajero", "fechaInicio": datetime.fromisoformat("2026-09-11"),"fechaFin":datetime.fromisoformat("2026-10-12")}
    return render(request, "templatesApp/templateModificarCampanias.html", {"campanias": campanias})

def renderTemplateEliminarCampanias(request):
    campania = {"nombre" : "El tunas puede"}
    return render(request, "templatesApp/templateEliminarCampania.html", {"campania":campania})

def renderTemplateCrearCampaniasOK(request):
    campanias=[
        {"nombre" : "Viltrum puede","presupuesto": 10000000, "descripcion": "Vamos a ayudar a la tierra y tu serás nuestro mensajero", "fechaInicio": datetime.fromisoformat("2026-09-11").isoformat(),"fechaFin":datetime.fromisoformat("2026-09-12").isoformat()}, 
        {"nombre" : "Jugar 2XOK(El TUKO)", "presupuesto": 8000000, "descripcion": "Te toca hacer 3 electrics al hilo con VI", "fechaInicio": datetime.fromisoformat("2026-10-11"),"fechaFin":datetime.fromisoformat("2026-10-12")},
               ]
    return render(request, "templatesApp/templateCrearCampaniaOK.html", {"campanias": campanias})

def renderTemplateModificarCampaniasOK(request):
    campanias = {"nombre" : "El tunas puede","presupuesto": 10000000, "descripcion": "Vamos a ayudar a la tierra y tu serás nuestro mensajero", "fechaInicio": datetime.fromisoformat("2026-09-11"),"fechaFin":datetime.fromisoformat("2026-10-12")}
    return render(request, "templatesApp/templateModificarCampaniasOK.html", {"campanias": campanias})

def renderTemplateEliminarCampaniaOK(request):
    return render(request, "templatesApp/templateEliminarCampaniaOK.html")



