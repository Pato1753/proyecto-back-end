from django.shortcuts import render

# Create your views here.
def renderMenuInicial(request):
    return render(request, "templatesApp/menuInicial.html")