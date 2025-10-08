from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from datetime import datetime

# Lista/diccionario de usuarios permitidos
# formato: usuario: (contraseña, rol)
USERS = {
    'empresa1': ('1234', 'EMPRESA'),
    'influencer': ('1234', 'INFLUENCER'),
}
INFLUENCER = {
    "influencer": {
        "password": "1234",
        "nombre": "Juan Pérez",
        "email": "juan@example.com",
        "red_social": "Instagram",
        "seguidores": 5000,
    }
}

def actualizar_influencer(request):
    username = "influencer"  # Aquí deberías sacar el usuario logueado de la sesión

    if request.method == "POST":
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        red_social = request.POST.get("red_social")
        seguidores = request.POST.get("seguidores")

        # Guardamos cambios en USERS
        INFLUENCER[username]["nombre"] = nombre
        INFLUENCER[username]["email"] = email
        INFLUENCER[username]["red_social"] = red_social
        INFLUENCER[username]["seguidores"] = seguidores

        print("Usuario actualizado: ",INFLUENCER[username])

        messages.success(request, "¡Datos actualizados correctamente!")
        return redirect("actualizar_influencer")

    return render(request, "templatesApp/actualizar_influencer.html", {
        "user": INFLUENCER[username]
    })
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

# render para campanias
def renderTemplatex(request):
    return render(request, "templatesApp/templatex.html")

def renderTemplateCrearCampanias(request):
    influencers = [
        {"nombreOpcion": 1, "opcionNombre": "Steven"},
        {"nombreOpcion": 2, "opcionNombre": "Lalo"},
    ]
    campanias = [
        {"nombreCampania": 1, "opcionCampania": "Viltrum te necesita"},
        {"nombreCampania": 2, "opcionCampania": "Lorem Ipsum"},
    ]
    status = [
        {"nombreStatus": 1, "opcionStatus": "Propuesta"},
        {"nombreStatus": 2, "opcionStatus": "Aceptada"},
        {"nombreStatus": 3, "opcionStatus": "En curso"},
        {"nombreStatus": 4, "opcionStatus": "Finalizada"},
    ]
    dias = [
        {"opcionNombre": "2026-09-11"},
        {"opcionNombre": "2026-10-16"},
        {"opcionNombre": "2026-09-01"},
    ]

    context = {
        "influencers": influencers,
        "campanias": campanias,
        "status": status,
        "dias": dias,
    }
    return render(request, "templatesApp/templateColaboracion.html", context)  # ✅ dict


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

# render para colaboracion
def renderTemplateColaboracion(request):
    influencers = [
        {"id": 1, "label": "Steven"},
        {"id": 2, "label": "Lalo"},
    ]
    campanias = [
        {"id": 1, "label": "Viltrum te necesita"},
        {"id": 2, "label": "Lorem Ipsum"},
    ]
    estados = [
        {"id": 1, "label": "Propuesta"},
        {"id": 2, "label": "Aceptada"},
        {"id": 3, "label": "En curso"},
        {"id": 4, "label": "Finalizada"},
    ]
    dias = [
        {"id": "2026-09-11", "label": datetime.fromisoformat("2026-09-11")},
        {"id": "2026-10-16", "label": datetime.fromisoformat("2026-10-16")},
        {"id": "2026-09-01", "label": datetime.fromisoformat("2026-09-01")},
    ]
    
    colaboraciones = [
        {
            "influencer": "Steven",
            "campania": "Viltrum te necesita",
            "status": "Propuesta",
            "pagoAcordado": 1000000,
            "diaAsignado": datetime.fromisoformat("2026-09-11"),
        }
    ]
    
    contexto = {
    "influencers": influencers,
    "campanias": campanias,
    "status": estados,
    "dias": dias,
    "colaboraciones": colaboraciones
    }   
    
    return render(request, "templatesApp/templateColaboracion.html", contexto)



def renderTemplateColaboracionCrear(request):
    
    influencers = [
        {"nombreOpcion": 1, "opcionNombre": "Steven"},
        {"nombreOpcion": 2, "opcionNombre": "Lalo"},
    ]
    campanias = [
        {"nombreCampania": 1, "opcionCampania": "Viltrum te necesita"},
        {"nombreCampania": 2, "opcionCampania": "Lorem Ipsum"},
    ]
    status = [
        {"nombreStatus": 1, "opcionStatus": "Propuesta"},
        {"nombreStatus": 2, "opcionStatus": "Aceptada"},
        {"nombreStatus": 3, "opcionStatus": "En curso"},
        {"nombreStatus": 4, "opcionStatus": "Finalizada"},
    ]


    context = {
        "influencers": influencers,
        "campanias": campanias,
        "status": status,

    }
    return render(request, "templatesApp/templateColaboracionCrear.html", context) 

def renderTemplateModificarColaboracion(request):
    return render(request, "templatesApp/templateColaboracionModificar.html")

def renderTemplateEliminarColaboracion(request):
    return render(request, "templatesApp/templateColaboracionElimina.html")

def renderTemplateColaboracionCrearOK(request):
    return render(request, "templatesApp/templateColaboracionCrearOK.html")

def renderTemplateModificarColaboracionOK(request):
    return render(request, "templatesApp/templateModificarColaboracionOK.html")

def renderTemplateEliminarColaboracionOK(request):
    return render(request, "templatesApp/templateEliminarColaboracionOK.html")




