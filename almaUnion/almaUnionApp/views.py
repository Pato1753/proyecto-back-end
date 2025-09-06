from django.shortcuts import render

# Create your views here.
def renderMenuInicial(request):
    return render(request, "templatesApp/menuInicial.html")

def renderRegEmpresa(request):
    return render(request, "templatesApp/regEmpresa.html")