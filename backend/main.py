# Importación del objeto FastAPI
from fastapi import FastAPI

# Creación de la instancia del objeto
app = FastAPI()

# READ - Ruta base de hola mundo
@app.get("/")
async def holaMundo():
    return {"mensaje": "Hola Mundo!"}