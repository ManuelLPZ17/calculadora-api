def suma(a: float, b: float) -> float:
    return a + b

def resta(a: float, b: float) -> float:
    return a - b

def multiplicacion(a: float, b: float) -> float:
    return a * b

def division(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b