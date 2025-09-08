from django.shortcuts import render

# Create your views here.
def renderTemplateMenuInicial(request):
    return render(request, "templatesApp/templateMenuInicial.html")

def renderTemplateRegistroEmpresa(request):
    return render(request, "templatesApp/templateRegistroEmpresa.html")

def renderTemplateRegistroInfluencer(request):
    return render(request, "templatesApp/templateRegistroInfluencer.html")

def renderTemplateHubEmpresa(request):
    return render(request, "templatesApp/templateHubEmpresa.html")

def renderTemplateHubInfluencer(request):
    return render(request, "templatesApp/templateHubInfluencer.html")