from django.core.management.base import BaseCommand
from usuarios.models import RolesUsuarios

class Command(BaseCommand):
    help = 'Carga roles iniciales en la base de datos'

    def handle(self, *args, **kwargs):
        roles = ['admin', 'customer']
        for rol in roles:
            RolesUsuarios.objects.get_or_create(nombre=rol)
        self.stdout.write(self.style.SUCCESS('Roles creados exitosamente.'))
