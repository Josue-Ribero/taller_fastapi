from sqlmodel import SQLModel, Field, Relationship
from ..utils.enums import EstadoCita
from typing import Optional
from datetime import datetime as dt

# Modelo base de cita
class CitaBase(SQLModel):
    fecha: dt = Field(default_factory=dt.now)
    hora: dt = Field(default_factory=dt.hour)
    costo: float = Field(default=0)
    estado: EstadoCita = Field(default=EstadoCita.PENDIENTE)

# Modelo de cita con ID autoincrementable
class Cita(CitaBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    clienteID: int = Field(foreign_key="usuario.id")
    cliente: Optional["Usuario"] = Relationship(back_populates="citasCliente")
    tecnicoID: int = Field(foreign_key="usuario.id")
    tecnico: Optional["Usuario"] = Relationship(back_populates="citasTecnico")
    vehiculoID: int = Field(foreign_key="vehiculo.id")
    vehiculo: Optional["Vehiculo"] = Relationship(back_populates="cita")

# Modelos de creación, actualización y eliminación de citas
class CitaCreate(CitaBase):
    pass

class CitaUpdate(CitaBase):
    pass

class CitaDelete(CitaBase):
    pass

# Importaciones diferidas
from ..models.usuario import Usuario
from ..models.vehiculo import Vehiculo