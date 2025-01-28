from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class UsuarioPersonalizado(AbstractUser):
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username


###no esta funcionado las migraciones por que hay un usuario ya creado y eso esta generDO EL PROBLEMA  lo mas seguro