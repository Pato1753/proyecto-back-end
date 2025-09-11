from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

# Lista/diccionario de usuarios permitidos
# formato: usuario: (contraseña, rol)
USERS = {
    'empresa1': ('1234', 'EMPRESA'),
    'influencer': ('1234', 'INFLUENCER'),
}

def renderTemplateMenuInicial(request):
    return render(request, "templatesApp/templateMenuInicial.html")

def renderTemplateRegistroEmpresa(request):
    return render(request, "templatesApp/templateRegistroEmpresa.html")

@csrf_protect
def renderTemplateRegistroInfluencer(request):
    return render(request, "templatesApp/templateRegistroInfluencer.html")

def renderTemplateHubEmpresa(request):
    infoPerfil = {"fotoPerfil": "assets/avatarEmpresa.png", "nombrePerfil": "Patricio Patoso"}
    botones = [
        {"label": "Inicio", "viewName": "inicio", "sourceImagen":"assets/casa.png", "sourceAlternative": "inicioLogo"},
        {"label": "Influencers", "viewName": "influencers", "sourceImagen":"assets/users.png", "sourceAlternative": "influencersLogo"},
        {"label": "Campañas", "viewName": "campanias", "sourceImagen":"assets/metricas.png", "sourceAlternative": "campañaLogo"},
        {"label": "Perfil", "viewName": "perfil", "sourceImagen":"assets/user.png", "sourceAlternative": "userLogo"},
        {"label": "Mensajes", "viewName": "mensajes", "sourceImagen":"assets/burbuja.png", "sourceAlternative": "mensajeLogo"},
        {"label": "Pagos", "viewName": "pagos", "sourceImagen":"assets/tarjetaDeBanco.png", "sourceAlternative": "pagosLogo"},
        {"label": "Configuración", "viewName": "configuracion", "sourceImagen":"assets/ajustes.png", "sourceAlternative": "configuraciónLogo"},
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

# Render del login con validación
def renderTemplatesLogin(request):
    error = None
    if request.method == "POST":
        username = request.POST.get("correo")
        password = request.POST.get("password")

        if username in USERS and USERS[username][0] == password:
            rol = USERS[username][1]

            if rol == "EMPRESA":
                return redirect("hubEmpresa")  # <-- nombre de la url del hub empresa
            elif rol == "INFLUENCER":
                return redirect("hubInfluencer")  # <-- nombre de la url del hub influencer
        else:
            error = "Usuario o contraseña incorrectos"

    return render(request, "templatesApp/templateLoginInflu.html", {"error": error})

def renderTemplateOportunidades(request):
    return render(request, "templatesApp/templateOportunidades.html")

def renderTemplateInformes(request):
    return render(request, "templatesApp/templateInformes.html")

# Render para Empresa
def renderTemplateInfluencers(request):
    return render(request, "templatesApp/templateInfluencers.html")

def renderTemplateCampanias(request):
    return render(request, "templatesApp/templateCampanias.html")

def renderTemplateMensajes(request):
    return render(request, "templatesApp/templateMensajes.html")

def renderTemplatePagos(request):
    return render(request, "templatesApp/templatePagos.html")
