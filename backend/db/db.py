# Importaciones de librerías y módulos
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from typing import Annotated

# Nombre, URL y motor de la DB
db_name = "taller.sqlite3"
db_url = f"sqlite:///{db_name}"
engine = create_engine(db_url)

# Crear todas las tablas de la DB
def createAllTables(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

# Obtener la sesión de la DB
def getSession():
    with Session(engine) as session:
        yield session

# Dependencias de la sesión de la DB
SessionDep = Annotated[Session, Depends(getSession)]