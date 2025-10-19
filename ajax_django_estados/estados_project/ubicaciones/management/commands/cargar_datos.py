from django.core.management.base import BaseCommand
from ubicaciones.models import Estado, Municipio

class Command(BaseCommand):
    help = "Carga todos los estados y municipios principales de México"

    def handle(self, *args, **kwargs):
        datos = {
            "Aguascalientes": ["Aguascalientes", "Jesús María", "Calvillo"],
            "Baja California": ["Mexicali", "Tijuana", "Ensenada", "Tecate", "Rosarito"],
            "Baja California Sur": ["La Paz", "Los Cabos", "Comondú", "Loreto", "Mulegé"],
            "Campeche": ["Campeche", "Carmen", "Champotón", "Escárcega"],
            "Coahuila": ["Saltillo", "Torreón", "Monclova", "Piedras Negras"],
            "Colima": ["Colima", "Manzanillo", "Tecomán"],
            "Chiapas": ["Tuxtla Gutiérrez", "San Cristóbal de las Casas", "Tapachula", "Comitán"],
            "Chihuahua": ["Chihuahua", "Ciudad Juárez", "Delicias", "Cuauhtémoc"],
            "Ciudad de México": ["Álvaro Obregón", "Iztapalapa", "Coyoacán", "Gustavo A. Madero", "Benito Juárez"],
            "Durango": ["Durango", "Gómez Palacio", "Lerdo"],
            "Guanajuato": ["León", "Irapuato", "Celaya", "Guanajuato", "Silao"],
            "Guerrero": ["Acapulco", "Chilpancingo", "Iguala", "Taxco"],
            "Hidalgo": ["Pachuca", "Tulancingo", "Tula de Allende", "Ixmiquilpan"],
            "Jalisco": ["Guadalajara", "Zapopan", "Tlaquepaque", "Puerto Vallarta", "Tonalá"],
            "México": ["Toluca", "Ecatepec", "Naucalpan", "Tlalnepantla", "Nezahualcóyotl"],
            "Michoacán": ["Morelia", "Uruapan", "Zamora", "Lázaro Cárdenas"],
            "Morelos": ["Cuernavaca", "Jiutepec", "Cuautla", "Temixco"],
            "Nayarit": ["Tepic", "Bahía de Banderas", "Compostela", "Santiago Ixcuintla"],
            "Nuevo León": ["Monterrey", "San Nicolás", "Guadalupe", "Apodaca", "Santa Catarina"],
            "Oaxaca": ["Oaxaca de Juárez", "Salina Cruz", "Juchitán", "Tuxtepec"],
            "Puebla": ["Puebla de Zaragoza", "Cholula", "Atlixco", "Tehuacán"],
            "Querétaro": ["Querétaro", "San Juan del Río", "El Marqués"],
            "Quintana Roo": ["Cancún", "Chetumal", "Playa del Carmen", "Cozumel", "Tulum"],
            "San Luis Potosí": ["San Luis Potosí", "Soledad", "Ciudad Valles", "Matehuala"],
            "Sinaloa": ["Culiacán", "Mazatlán", "Los Mochis", "Guasave"],
            "Sonora": ["Hermosillo", "Ciudad Obregón", "Nogales", "Navojoa"],
            "Tabasco": ["Villahermosa", "Cárdenas", "Comalcalco", "Macuspana"],
            "Tamaulipas": ["Tampico", "Ciudad Victoria", "Reynosa", "Matamoros", "Nuevo Laredo"],
            "Tlaxcala": ["Tlaxcala", "Apizaco", "Huamantla"],
            "Veracruz": ["Xalapa", "Veracruz", "Coatzacoalcos", "Poza Rica", "Orizaba"],
            "Yucatán": ["Mérida", "Valladolid", "Tizimín", "Progreso"],
            "Zacatecas": ["Zacatecas", "Fresnillo", "Jerez", "Guadalupe"],
        }

        for estado_nombre, municipios in datos.items():
            estado, _ = Estado.objects.get_or_create(nombre=estado_nombre)
            for m in municipios:
                Municipio.objects.get_or_create(nombre=m, estado=estado)

        self.stdout.write(self.style.SUCCESS("Datos cargados correctamente"))
