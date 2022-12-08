from xmlrpc.client import FastMarshaller
from fastapi import FastAPI
import json

# cambio 
app=FastAPI()

datos = {"1":"Python", "2":"Java", "3":"PHP","4": "Javascript","5":"Panchi"}

@app.get("/")
def raiz():
    sin_codificar = json.dumps(datos)
    return json.loads(sin_codificar)

@app.get("/validar/{numero}")
def validar_capicua (numero:str):
    respuesta = 'No es capicua'
    if numero == numero[::-1]:
        respuesta = 'Es capicua'
    
    return {"numero": numero,
            "validacion": respuesta} 

@app.post("/students")
def guardar(name:str, lastname:str):
    return f"Estudiante {name} {lastname} guardado!"