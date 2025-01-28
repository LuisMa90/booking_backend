from django.urls import path
from .views import RegistroUsuarioView, ListaUsuariosView, UsuarioDetalleView

urlpatterns = [
    path('registro/', RegistroUsuarioView.as_view(), name='registro'),
    path('usuarios/', ListaUsuariosView.as_view(), name='usuarios'),
    path('usuarios/<int:pk>/', UsuarioDetalleView.as_view(), name='usuario-detalle'),
]
