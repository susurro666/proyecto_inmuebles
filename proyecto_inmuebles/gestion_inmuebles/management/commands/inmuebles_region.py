from django.core.management.base import BaseCommand
from gestion_inmuebles.models import Inmueble
import csv


class Command(BaseCommand):
    help = "TRAE INFORMACIÓN SOBRE INMUEBLES EN BASE A UNA REGIÓN"

    def add_arguments(self, parser):
        parser.add_argument(
            "nombre_archivo",
            type=str,
            help="El nombre del archivo donde se va a guardar la información",
        )
        parser.add_argument(
            "region",
            type=str,
            help="El nombre de la región a filtrar",
        )

    def handle(self, *args, **options):
        nombre_archivo = options["nombre_archivo"]
        region = options["region"]
        listado = Inmueble.objects.filter(comuna__region__nombre__icontains=region)
        with open(nombre_archivo, mode="w", encoding="utf-8", newline="") as archivo:
            writer = csv.DictWriter(archivo, fieldnames={"nombre", "descripción"})
            writer.writeheader()
            for inmueble in listado:
                writer.writerow(
                    {"nombre": inmueble.nombre, "descripción": inmueble.descripcion}
                )

        self.stdout.write(
            self.style.SUCCESS(f"Se ha escrito la información en {nombre_archivo}")
        )