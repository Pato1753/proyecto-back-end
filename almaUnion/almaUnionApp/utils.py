from functools import wraps
from django.shortcuts import redirect
from django.http import HttpResponseForbidden

def sessionInicioRequerida(vista):
    @wraps(vista)
    def _wrapped(request, *args, **kwargs):
        if not request.session.get("uid"):
            return redirect("login")
        return vista(request, *args, **kwargs)
    return _wrapped

def rolRequerido(rolEsperado):
    def decorator(vista):
        @wraps(vista)
        def _wrapped(request, *args, **kwargs):
            if request.session.get("rol") != rolEsperado:
                return HttpResponseForbidden("No autorizado para ese hub.")
            return vista(request, *args, **kwargs)
        return _wrapped
    return decorator