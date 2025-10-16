from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.db import transaction
from django.urls import reverse

from almaUnionApp.models import Usuarios
from almaUnionApp.choices.RolChoices import RolChoices
from almaUnionApp.forms.RegistroEmpresaForm import (RegistroUsuarioForm as RegistroUsuarioFormEm,
                                                    RegistroEmpresaForm as RegistroEmpresaFormEm,
                                                    RegistroRedesSocialesForm as RegistroRedesSocialesFormEm)
from almaUnionApp.forms.RegistroInfluencerForm import (RegistroUsuarioForm as RegistroUsuarioFormIn,
                                                       RegistroInfluencerForm as RegistroInfluencerFormIn,
                                                       RegistroRedesSocialesForm as RegistroRedesSocialesFormIn)
from almaUnionApp.forms.InicioSesionForm import InicioForm as iniForm
from .utils import sessionInicioRequerida, rolRequerido

from datetime import datetime
from django.contrib import messages


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



def renderTemplateMenuInicial(request):
    return render(request, "templatesApp/templateMenuInicial.html")

@transaction.atomic
def renderTemplateRegistroEmpresa(request):
    if request.method == "POST" and "submit_empresa" in request.POST:
        empresaForm = RegistroEmpresaFormEm(request.POST)
        usuarioForm = RegistroUsuarioFormEm(request.POST)
        redesSocialesForm = RegistroRedesSocialesFormEm(request.POST)

        if empresaForm.is_valid() and usuarioForm.is_valid() and redesSocialesForm.is_valid():

            empresa = empresaForm.save()
            
            usuario = usuarioForm.save(commit=False)
            usuario.rol = RolChoices.EMPRESA          
            usuario.id_empresa_usuarios = empresa.id_empresa  
            usuario.id_influencer_usuarios = None
            usuario.save()
            
            redesSociales = redesSocialesForm.save(commit=False)
            redesSociales.id_empresa_redes = empresa.id_empresa
            redesSociales.id_influencer_redes = None
            redesSociales.save()
            
            messages.success(request, "Empresa registrada correctamente")
            return redirect("login")
        else:
                messages.error(request, "Revisa los datos ingresados")
    else:
        empresaForm = RegistroEmpresaFormEm()
        usuarioForm = RegistroUsuarioFormEm()
        redesSocialesForm = RegistroRedesSocialesFormEm()
                
    return render(request, "templatesApp/templateRegistroEmpresa.html", { 
        "empresaForm": empresaForm,
        "usuarioForm": usuarioForm,
        "redesSocialesForm": redesSocialesForm
    })
        
@transaction.atomic
def renderTemplateRegistroInfluencer(request):
    if request.method == 'POST' and "submit_influencer" in request.POST:
        usuarioForm = RegistroUsuarioFormIn(request.POST)
        influencerForm = RegistroInfluencerFormIn(request.POST)
        redesSocialesForm = RegistroRedesSocialesFormIn(request.POST)
        
        if usuarioForm.is_valid() and influencerForm.is_valid() and redesSocialesForm.is_valid():
            influencer = influencerForm.save()
            
            usuario = usuarioForm.save(commit=False)
            usuario.rol = RolChoices.INFLUENCER         
            usuario.id_influencer_usuarios = influencer.id_influencer
            usuario.id_empresa_usuarios = None
            usuario.save()
            
            redesSociales = redesSocialesForm.save(commit=False)
            redesSociales.id_influencer_redes = influencer.id_influencer
            redesSociales.id_empresa_redes = None
            redesSociales.save()
            
            messages.success(request, "Influencer registrado correctamente")
            return redirect("login")
        else:
            messages.error(request, "Revisa los datos ingresados")
    else:
        usuarioForm = RegistroUsuarioFormIn()
        influencerForm = RegistroInfluencerFormIn()
        redesSocialesForm = RegistroRedesSocialesFormIn()

    return render(request, "templatesApp/templateRegistroInfluencer.html", {
        "usuarioForm": usuarioForm,
        "influencerForm": influencerForm,
        "redesSocialesForm": redesSocialesForm
    })

@sessionInicioRequerida
@rolRequerido(RolChoices.INFLUENCER)
def actualizar_influencer(request):
    # Tu lógica de actualización
    pass

@transaction.atomic
def renderTemplateInicio(request):
    if request.method == "POST" and "submit_inicio" in request.POST:
        inicioForm = iniForm(request.POST)

        if inicioForm.is_valid():
            email = inicioForm.cleaned_data["email"].strip().lower()
            contrasena = inicioForm.cleaned_data["contrasena"]

            # Buscar usuario por email (case-insensitive)
            try:
                usuario = Usuarios.objects.get(email__iexact=email)
            except Usuarios.DoesNotExist:
                messages.error(request, "Correo o contraseña inválidos.")
                return render(request, "templatesApp/templateLogin.html", {"inicioForm": inicioForm})

            # Validar contraseña hasheada
            if not check_password(contrasena, usuario.contrasena):
                messages.error(request, "Correo o contraseña inválidos.")
                return render(request, "templatesApp/templateLogin.html", {"inicioForm": inicioForm})

            # Sesión “custom”
            request.session.cycle_key()
            request.session["uid"] = usuario.id_usuario
            request.session["email"] = usuario.email
            request.session["rol"] = usuario.rol
            request.session.set_expiry(60 * 60 * 4)  # 4 horas

            # Redirección por rol
            if usuario.rol == RolChoices.EMPRESA:
                messages.success(request, "¡Bienvenido!")
                return redirect(reverse("hubEmpresa"))
            elif usuario.rol == RolChoices.INFLUENCER:
                messages.success(request, "¡Bienvenido!")
                return redirect(reverse("hubInfluencer"))
            else:
                messages.warning(request, "No se encontró rol. Te llevamos al inicio.")
                return redirect("inicio")

        # <-- Este else corresponde a inicioForm.is_valid()
        messages.error(request, "Por favor corrige los errores del formulario.")
        return render(request, "templatesApp/templateLogin.html", {"inicioForm": inicioForm})

    # GET u otros casos
    inicioForm = iniForm()
    return render(request, "templatesApp/templateLogin.html", {"inicioForm": inicioForm})

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

@sessionInicioRequerida
@rolRequerido(RolChoices.EMPRESA)
def renderTemplateHubEmpresa(request):
    uid = request.session["uid"]
    usuario = (Usuarios.objects
               .only("id_usuario", "email", "rol", "id_empresa_usuarios")
               .get(id_usuario=uid))
    
    empresa = usuario.id_empresa_usuarios
    if not empresa:
        return render(request, "templatesApp/hubEmpresa_vacio.html", {"usuario": usuario})
    """ Datos base del perfil """
    return render(request, "templatesApp/templateHubEmpresa.html", {"usuario": usuario})
    
@sessionInicioRequerida
@rolRequerido(RolChoices.INFLUENCER)
def renderTemplateHubInfluencer(request):
    uid = request.session["uid"]
    
    usuario = (Usuarios. objects
               .only("id_usuario", "email", "rol", "id_influencer_usuarios")
               .get(id_usuario=uid))
    influencer = usuario.id_influencer_usuarios
    if not influencer:
        return render(request, "templatesApp/hubInfluencerVacio.html", {"usuario": usuario})
    # Datos base del perfil
    
    return render(request, "templatesApp/templateHubInfluencer.html", {"usuario": usuario})

# Render en común influencer-Empresa
def renderTemplateConfiguracion(request):
    return render(request, "templatesApp/templateConfiguracion.html")

def renderTemplatePerfil(request):
    return render(request, "templatesApp/templatePerfil.html")

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

def renderTemplateRedesSociales(request):
    return render(request, "templatesApp/templateRedesSociales.html")
        
def renderTemplateRedesSocialesCrear(request):
    return render(request, "templatesApp/templateRedesSocialesCrear.html")

def renderTemplateRedesSocialesModificar(request):
    return render(request, "templatesApp/templateRedesSocialesModificar.html")

def renderTemplateRedesSocialesEliminar(request):
    return render(request, "templatesApp/templateRedesSocialesEliminar.html")

