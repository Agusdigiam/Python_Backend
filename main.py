from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Hola Mundo"

@app.get("/url")
async def root():
    return {"url" : "https://www.google.com.ar/"}