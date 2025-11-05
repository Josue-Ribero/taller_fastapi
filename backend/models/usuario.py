from sqlmodel import SQLModel, Field, Relationship
from ..utils.enums import RolUsuario
from typing import Optional
from pydantic import EmailStr
from datetime import datetime as dt

# Modelo base de usuario
class UsuarioBase(SQLModel):
    nombre: Optional[str] = Field(default=None)
    apellido: Optional[str] = Field(default=None)
    email: EmailStr = Field(unique=True, index=True)
    telefono: Optional[str] = Field(default=None)
    direccion: Optional[str] = Field(default=None)
    contraseña: str = Field(min_length=6)
    rol: RolUsuario = Field(default=RolUsuario.ADMIN)
    fechaRegistro: dt = Field(default_factory=dt.now)
    activo: bool = Field(default=True)
    eliminado: bool = Field(default=False)

# Modelo de usuario con ID autoincrementable
class Usuario(UsuarioBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    citasCliente: list["Cita"] = Relationship(back_populates="cliente")
    citasTecnico: list["Cita"] = Relationship(back_populates="tecnico")
    bateria: Optional["Bateria"] = Relationship(back_populates="Usuario", sa_relationship_kwargs={"uselist": False})
    citas: list["Cita"] = Relationship(back_populates="Usuario")

# Modelos de creación, actualización y eliminación de usuarios
class UsuarioCreate(UsuarioBase):
    pass

class UsuarioUpdate(UsuarioBase):
    pass

class UsuarioDelete(UsuarioBase):
    pass

# Importaciones diferidas
from ..models.bateria import Bateria
from ..models.cita import Cita