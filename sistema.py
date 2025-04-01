import random

def leer_datos_sensor():
    """
    Simula la lectura de un sensor de temperatura.
    Retorna un valor entre -10 y 40 grados Celsius.
    """
    return round(random.uniform(-10, 40), 2)

def convertir_a_fahrenheit(celsius):
    """
    Convierte grados Celsius a Fahrenheit.
    """
    if not isinstance(celsius, (int, float)):
        raise ValueError("El valor debe ser numérico.")
    return round(celsius * 9 / 5 + 32, 2)

def registrar_datos(celsius):
    """
    Procesa los datos del sensor:
    - Lee temperatura (°C)
    - Convierte a °F
    - Devuelve un diccionario con ambos valores
    """
    temperatura_f = convertir_a_fahrenheit(celsius)
    return {
        "celsius": celsius,
        "fahrenheit": temperatura_f
    }