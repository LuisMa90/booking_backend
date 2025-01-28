from statistics import mode
from django.db import models

from django.contrib.auth.models import AbstractUser, Permission
from django.db import models


class RolesUsuarios(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    permisos = models.ManyToManyField(Permission, blank=True)

    def __str__(self):
        return self.nombre

class UsuarioPersonalizado(AbstractUser):
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    rol = models.ForeignKey(RolesUsuarios, on_delete=models.SET_NULL, null=True, blank=True, related_name="usuarios")

    class meta:
        class Meta:
            permissions = [
                ("can_view_dashboard", "Puede ver el dashboard"),
                ("can_manage_users", "Puede gestionar usuarios"),
            ]

    def has_perm(self, perm, obj=None):
        if self.is_superuser:
            return True
        if self.rol and self.rol.permisos.filter(codename=perm.split('.')[-1]).exists():
            return True
        return False

    def __str__(self):
        return self.username

class RegistroActividad(models.Model):
    usuario = models.ForeignKey(UsuarioPersonalizado, on_delete=models.CASCADE)
    accion = models.CharField(max_length=255)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} - {self.accion} - {self.fecha}"
