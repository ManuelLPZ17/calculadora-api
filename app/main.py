from fastapi import FastAPI, HTTPException
from .operations import suma, resta, multiplicacion, division
#comentarios
app = FastAPI(title="Calculadora API")

@app.get("/")
def root():
    return {"message": "Calculadora API funcionando"}

@app.get("/suma")
def endpoint_suma(a: float, b: float):
    return {"operacion": "suma", "a": a, "b": b, "resultado": suma(a, b)}

@app.get("/resta")
def endpoint_resta(a: float, b: float):
    return {"operacion": "resta", "a": a, "b": b, "resultado": resta(a, b)}

@app.get("/multiplicacion")
def endpoint_multiplicacion(a: float, b: float):
    return {"operacion": "multiplicacion", "a": a, "b": b, "resultado": multiplicacion(a, b)}

@app.get("/division")
def endpoint_division(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="No se puede dividir entre cero")
    return {"operacion": "division", "a": a, "b": b, "resultado": division(a, b)}