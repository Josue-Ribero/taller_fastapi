from sqlmodel import SQLModel, Field, Relationship
from ..utils.enums import MarcaVehiculo, EstadoVehiculo
from typing import Optional

# Modelo base de vehiculo
class VehiculoBase(SQLModel):
    marca: MarcaVehiculo = Field(default=MarcaVehiculo.TESLA)
    modelo: Optional[str] = Field(default=None)
    anio: Optional[int] = Field(default=0)
    imagenUrl: Optional[str] = Field(default=None)
    estado: EstadoVehiculo = Field(default=EstadoVehiculo.EN_TALLER)
    eliminado: Optional[bool] = Field(default=False)

# Modelo de vehiculo con ID autoincrementable
class Vehiculo(VehiculoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    bateria: Optional["Bateria"] = Relationship(back_populates="vehiculo", sa_relationship_kwargs={"uselist": False})
    citas: list["Cita"] = Relationship(back_populates="vehiculo")

# Modelos de creación, actualización y eliminación de vehiculos
class VehiculoCreate(VehiculoBase):
    pass

class VehiculoUpdate(VehiculoBase):
    pass

class VehiculoDelete(VehiculoBase):
    pass

# Importaciones diferidas
from ..models.bateria import Bateria
from ..models.cita import Cita