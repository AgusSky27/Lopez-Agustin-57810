from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

# Create your views here.
def home(request):
    return render(request, "Unidades/index.html")


def Acerca(request):
    return render(request, "Unidades/acerca.html")

#___________Costa
@login_required
def CostaTraful(request):
    contexto = {"costa": Costa.objects.all()}
    return render(request, "Unidades/costa.html", contexto)

@login_required
def costaForm(request):
    if request.method == "POST":
        miForm = CostaForm(request.POST)
        if miForm.is_valid():
            costa_nombre = miForm.cleaned_data.get("nombre")
            costa_apellido = miForm.cleaned_data.get("apellido")
            costa_cabaña = miForm.cleaned_data.get("cabaña")
            costa_fechaEstadia = miForm.cleaned_data.get("fechaEstadia")
            costa = Costa(nombre=costa_nombre, apellido=costa_apellido, cabaña=costa_cabaña, fechaEstadia=costa_fechaEstadia)
            costa.save()
            contexto = {"costa": Costa.objects.all() }
            return render(request, "Unidades/costa.html", contexto)
    else:
        miForm = CostaForm()
    return render(request, "Unidades/costaForm.html", {"form": miForm})

@login_required
def buscarReservaCosta(request):
    return render(request, "Unidades/buscar.html")

@login_required
def encontrarReservaCosta(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        costa = Costa.objects.filter(nombre__icontains=patron)
        contexto ={'costa': costa}
    else:
        contexto ={'costa': Costa.objects.all()}

    return render(request, "Unidades/costa.html", contexto)

@login_required
def costaUpdate(request, id_costa):
    costa= Costa.objects.get(id=id_costa)
    if request.method == "POST":
        miForm = CostaForm(request.POST)
        if miForm.is_valid():
            costa.nombre = miForm.cleaned_data.get("nombre")
            costa.apellido = miForm.cleaned_data.get("apellido")
            costa.cabaña = miForm.cleaned_data.get("cabaña")
            costa.fechaEstadia = miForm.cleaned_data.get("fechaEstadia")
            costa.save()
            contexto = {"costa": Costa.objects.all() }
            return render(request, "Unidades/costa.html", contexto)
    else:
        miForm = CostaForm(initial={"nombre": costa.nombre, "apellido": costa.apellido, "cabaña": costa.cabaña, "fechaEstadia": costa.fechaEstadia})
    return render(request, "Unidades/costaForm.html", {"form": miForm})

@login_required
def costaDelete(request, id_costa):
    costa = Costa.objects.get(id=id_costa)
    costa.delete()
    contexto = {"costa": Costa.objects.all() }
    return render(request, "Unidades/costa.html", contexto)


#_____________Natur
@login_required
def NaturHaus(request):
    contexto = {"natur": Natur.objects.all()}
    return render(request, "Unidades/natur.html", contexto)

@login_required
def naturForm(request):
    if request.method == "POST":
        miForm = NaturForm(request.POST)
        if miForm.is_valid():
            natur_nombre = miForm.cleaned_data.get("nombre")
            natur_apellido = miForm.cleaned_data.get("apellido")
            natur_cabaña = miForm.cleaned_data.get("cabaña")
            natur_fechaEstadia = miForm.cleaned_data.get("fechaEstadia")
            natur = Natur(nombre=natur_nombre, apellido=natur_apellido, cabaña=natur_cabaña, fechaEstadia=natur_fechaEstadia)
            natur.save()
            contexto = {"natur": Natur.objects.all() }
            return render(request, "Unidades/natur.html", contexto)
    else:
        miForm = NaturForm()
    return render(request, "Unidades/naturForm.html", {"form": miForm})

@login_required
def naturUpdate(request, id_natur):
    natur = Natur.objects.get(id=id_natur)
    if request.method == "POST":
        miForm = NaturForm(request.POST)
        if miForm.is_valid():
            natur.nombre = miForm.cleaned_data.get("nombre")
            natur.apellido = miForm.cleaned_data.get("apellido")
            natur.cabaña = miForm.cleaned_data.get("cabaña")
            natur.fechaEstadia = miForm.cleaned_data.get("fechaEstadia")
            natur.save()
            contexto = {"natur": Natur.objects.all() }
            return render(request, "Unidades/natur.html", contexto)
    else:
        miForm = NaturForm(initial={"nombre": natur.nombre, "apellido": natur.apellido, "cabaña": natur.cabaña, "fechaEstadia": natur.fechaEstadia})
    return render(request, "Unidades/naturForm.html", {"form": miForm})

@login_required
def naturDelete(request, id_natur):
    natur = Natur.objects.get(id=id_natur)
    natur.delete()
    contexto = {"natur": Natur.objects.all() }
    return render(request, "Unidades/natur.html", contexto)

#___________Rayen
@login_required
def CabañasRayen(request):
    contexto = {"rayen": Rayen.objects.all()}
    return render(request, "Unidades/rayen.html", contexto)

@login_required
def rayenForm(request):
    if request.method == "POST":
        miForm = RayenForm(request.POST)
        if miForm.is_valid():
            rayen_nombre = miForm.cleaned_data.get("nombre")
            rayen_apellido = miForm.cleaned_data.get("apellido")
            rayen_cabaña = miForm.cleaned_data.get("cabaña")
            rayen_fechaEstadia = miForm.cleaned_data.get("fechaEstadia")
            rayen = Rayen(nombre=rayen_nombre, apellido=rayen_apellido, cabaña=rayen_cabaña, fechaEstadia=rayen_fechaEstadia)
            rayen.save()
            contexto = {"rayen": Rayen.objects.all() }
            return render(request, "Unidades/rayen.html", contexto)
    else:
        miForm = RayenForm()
    return render(request, "Unidades/rayenForm.html", {"form": miForm})

@login_required
def rayenUpdate(request, id_rayen):
    rayen = Rayen.objects.get(id=id_rayen)
    if request.method == "POST":
        miForm = RayenForm(request.POST)
        if miForm.is_valid():
            rayen.nombre = miForm.cleaned_data.get("nombre")
            rayen.apellido = miForm.cleaned_data.get("apellido")
            rayen.cabaña = miForm.cleaned_data.get("cabaña")
            rayen.fechaEstadia = miForm.cleaned_data.get("fechaEstadia")
            rayen.save()
            contexto = {"rayen": Rayen.objects.all() }
            return render(request, "Unidades/rayen.html", contexto)
    else:
        miForm = RayenForm(initial={"nombre": rayen.nombre, "apellido": rayen.apellido, "cabaña": rayen.cabaña, "fechaEstadia": rayen.fechaEstadia})
    return render(request, "Unidades/rayenForm.html", {"form": miForm})

@login_required
def rayenDelete(request, id_rayen):
    rayen = Rayen.objects.get(id=id_rayen)
    rayen.delete()
    contexto = {"rayen": Rayen.objects.all() }
    return render(request, "Unidades/rayen.html", contexto)

#___________Vulcanche

class VulcancheList(LoginRequiredMixin, ListView):
    model = Vulcanche

class VulcancheCreate(LoginRequiredMixin, CreateView):
    model = Vulcanche
    fields = ["nombre", "apellido", "cabaña", "fechaEstadia"]
    success_url = reverse_lazy("vulcanche")

class VulcancheUpdate(LoginRequiredMixin, UpdateView):
    model = Vulcanche
    fields = ["nombre", "apellido", "cabaña", "fechaEstadia"]
    success_url = reverse_lazy("vulcanche")

class VulcancheDelete(LoginRequiredMixin, DeleteView):
    model = Vulcanche
    success_url = reverse_lazy("vulcanche")


#____login / logout / registracion

def loginRequest(request):
    if request.method == "POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)

            #_____Buscar avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            #____________________
            return render(request, "Unidades/index.html")
        else:
            return redirect(reverse_lazy('login'))

    else:
        miForm = AuthenticationForm()

    return render(request, "Unidades/login.html", {"form": miForm})

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = RegistroForm()

    return render(request, "Unidades/register.html", {"form": miForm})

#____ EDICION DE PERFIL / AVATAR

@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy("home"))
    else:
        miForm = UserEditForm(instance=usuario)
    return render(request, "Unidades/editProfile.html", {"form": miForm})

class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "Unidades/cambiar_clave.html"
    success_url = reverse_lazy("home")

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen = miForm.cleaned_data["imagen"]
            #________Borro avatares viejos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #___________________________________________
            avatar = Avatar(user=usuario, imagen=imagen)    
            avatar.save()
            #___________ Enviar la imagen al home
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            #___________________________________________
            return redirect(reverse_lazy("home"))
    else:
        miForm = AvatarForm()
    return render(request, "Unidades/agregarAvatar.html", {"form": miForm})
