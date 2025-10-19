from django.core.management.base import BaseCommand
from ubicaciones.models import Estado, Municipio

class Command(BaseCommand):
    help = "Carga estados y municipios de ejemplo"

    def handle(self, *args, **kwargs):
        datos = {
            "Estado de México": ["Toluca", "Ecatepec", "Naucalpan"],
            "Jalisco": ["Guadalajara", "Zapopan", "Tlaquepaque"],
            "Nuevo León": ["Monterrey", "San Nicolás", "Guadalupe"],
            "Puebla": ["Puebla de Zaragoza", "Cholula", "Atlixco"]
        }

        for estado_nombre, municipios in datos.items():
            estado, _ = Estado.objects.get_or_create(nombre=estado_nombre)
            for m in municipios:
                Municipio.objects.get_or_create(nombre=m, estado=estado)

        self.stdout.write(self.style.SUCCESS("✅ Datos cargados correctamente"))
