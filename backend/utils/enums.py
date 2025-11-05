# Enumeraciones de los modelos
from enum import Enum

class TipoBateria(str, Enum):
    LITIO_ION = "Litio-ion"
    PLOMO_ACIDO = "Plomo-ácido"
    NIMH = "NiMH"
    SOLIDA = "Sólida"


class EstadoBateria(str, Enum):
    DISPONIBLE = "Disponible"
    EN_USO = "En uso"
    EN_MANTENIMIENTO = "En mantenimiento"


class RolUsuario(str, Enum):
    ADMIN = "admin"
    TECNICO = "tecnico"
    CLIENTE = "cliente"


class MarcaVehiculo(str, Enum):
    TESLA = "Tesla"
    NISSAN = "Nissan"
    BMW = "BMW"
    RENAULT = "Renault"
    CHEVROLET = "Chevrolet"

class EstadoVehiculo(str, Enum):
    DISPONIBLE = "Disponible"
    EN_TALLER = "En taller"
    EN_MANTENIMIENTO = "En mantenimiento"


class EstadoCita(str, Enum):
    PENDIENTE = "Pendiente"
    EN_PROGRESO = "En progreso"
    COMPLETADA = "Completada"