from django.contrib.auth.models import Permission
from usuarios.models import Rol

# Crear un rol
admin_role, _ = Rol.objects.get_or_create(nombre='admin', descripcion='Administrador del sistema')

# Asignar permisos al rol
permiso_usuarios = Permission.objects.get(codename='view_user')  # Ver usuarios
permiso_gestion = Permission.objects.get(codename='change_user')  # Editar usuarios

admin_role.permisos.add(permiso_usuarios, permiso_gestion)
admin_role.save()