from sqlmodel import SQLModel, Field, Relationship
from ..utils.enums import EstadoBateria, TipoBateria
from typing import Optional

# Modelo base de bateria
class BateriaBase(SQLModel):
    codigo: Optional[str] = Field(default=None)
    tipo: TipoBateria = Field(default=TipoBateria.LITIO_ION)
    capacidadKwh: Optional[int] = Field(default=0)
    estadoSalud: Optional[float] = Field(default=0)
    ciclosCarga: Optional[int] = Field(default=0)
    temperaturaOperacion: Optional[float] = Field(default=None)
    estado: EstadoBateria = Field(default=EstadoBateria.DISPONIBLE)
    eliminado: Optional[bool] = Field(default=False)

# Modelo de bateria con ID autoincrementable
class Bateria(BateriaBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    vehiculoID: int = Field(foreign_key="vehiculo.id")
    vehiculo: "Vehiculo" = Relationship(back_populates="bateria")

# Modelos de creación, actualización y eliminación de baterias
class BateriaCreate(BateriaBase):
    pass

class BateriaUpdate(BateriaBase):
    pass

class BateriaDelete(BateriaBase):
    pass

# Importaciones diferidas
from ..models.vehiculo import Vehiculo