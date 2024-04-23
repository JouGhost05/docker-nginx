from fastapi import FastAPI

app = FastAPI()

@app.get("/api/saludo")
def read_root():
    return {"mensaje": "¡Hola desde FastAPI!"}
