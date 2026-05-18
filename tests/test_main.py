"""
Pruebas unitarias del proyecto
"""
from src.utils.helpers import saludar, calcular_anio_nacimiento

def test_saludar():
    assert saludar("Pablo") == "¡Hola, Pablo!"

def test_calcular_anio():
    assert calcular_anio_nacimiento(20) == 2006