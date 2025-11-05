from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def holaMundo():
    return {"mensaje": "Hola Mundo!"}