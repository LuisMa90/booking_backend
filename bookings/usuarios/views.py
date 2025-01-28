from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UsuarioPersonalizado, RolesUsuarios
from .serializers import UsuarioSerializer, RegistroUsuarioSerializer, RolesUsuariosSerializer
from rest_framework.permissions import IsAuthenticated

class RegistroUsuarioView(generics.CreateAPIView):
    serializer_class = RegistroUsuarioSerializer
    permission_classes = [permissions.AllowAny]

class ListaUsuariosView(generics.ListAPIView):
    queryset = UsuarioPersonalizado.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

class UsuarioDetalleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UsuarioPersonalizado.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

class ListaRolesView(generics.ListCreateAPIView):
    queryset = RolesUsuarios.objects.all()
    serializer_class = RolesUsuariosSerializer
    permission_classes = [permissions.IsAuthenticated]
