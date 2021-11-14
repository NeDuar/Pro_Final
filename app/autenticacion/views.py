from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import login, logout, authenticate
from . import views
from axes.models import *


def acceder(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=password)
            if usuario is not None:
                login(request, usuario)
                messages.success(request, F"Bienvenid@ de nuevo {nombre_usuario}")
                return redirect("listado_productos")
            else:
                messages.error(request, "Los datos son incorrectos")
        else:
            messages.error(request, "Los datos son incorrectos")

    form = AuthenticationForm()
    intentos = AccessAttempt.objects.all()
    context = {'intentos': intentos, "form": form}
    return render(request, "autenticacion/acceder.html", context)


class VistaRegistro(View):
    # noinspection PyMethodMayBeStatic
    def get(self, request):
        form = UserRegisterForm()
        return render(request, "autenticacion/registro.html", {"form": form})

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            nombre_usuario = form.cleaned_data.get("username")
            messages.success(request, F"Bienvenid@ a la plataforma {nombre_usuario}")
            login(request, usuario, backend='django.contrib.auth.backends.ModelBackend')
            return redirect("listado_productos")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "autenticacion/registro.html", {"form": form})


def salir(request):
    logout(request)
    messages.success(request, F"Tu sesión se ha cerrado correctamente")
    return redirect("acceder")
