from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    #_______ Home / Modulos / acerca
    path('', home, name="home"),
    path('acerca/', Acerca, name="acerca"),
    path('costa/', CostaTraful, name="costa"),
    path('natur/', NaturHaus, name="natur"),
    path('rayen/', CabañasRayen, name="rayen"),
    path('vulcanche/', VulcancheList.as_view(), name="vulcanche"),

    #formularios
    path('costaForm/', costaForm, name="costaForm"),
    path('rayenForm/', rayenForm, name="rayenForm"),
    path('naturForm/', naturForm, name="naturForm"),
    path('vulcancheCreate/', VulcancheCreate.as_view(), name="vulcancheCreate"),

    #buscar/encontrar
    path('buscarReservaCosta/', buscarReservaCosta, name="buscarReservaCosta"),
    path('encontrarReservaCosta/', encontrarReservaCosta, name="encontrar_reserva_costa"),

    #uptdate
    path('costaUpdate/<id_costa>/', costaUpdate, name="costaUpdate"),
    path('naturUpdate/<id_natur>/', naturUpdate, name="naturUpdate"),
    path('rayenUpdate/<id_rayen>/', rayenUpdate, name="rayenUpdate"),
    path('vulcancheUpdate/<int:pk>/', VulcancheUpdate.as_view(), name="vulcancheUpdate"),

    #DELETE
    path('costaDelete/<id_costa>/', costaDelete, name="costaDelete"),
    path('naturDelete/<id_natur>/', naturDelete, name="naturDelete"),
    path('rayenDelete/<id_rayen>/', rayenDelete, name="rayenDelete"),
    path('vulcancheDelete/<int:pk>/', VulcancheDelete.as_view(), name="vulcancheDelete"),

    #login / logout / registracion
    path('login/', loginRequest, name="login"),
    path('logout/', LogoutView.as_view(template_name="Unidades/logout.html"), name="logout"),
    path('register/', register, name="register"),

    #editar perfil
    path('editProfile/', editProfile, name="editProfile"),
    path('<int:pk>/password/', CambiarClave.as_view(), name="cambiarClave"),
    path('agregarAvatar/', agregarAvatar, name="agregarAvatar"),

]