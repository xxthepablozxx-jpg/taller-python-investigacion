# Investigación: Conceptos Básicos de Python

## 1. ¿Qué es una variable en Python?

Una variable es un espacio en memoria que almacena un valor con un nombre.

Tipos de datos:
- **Enteros** (`int`): `edad = 20`
- **Flotantes** (`float`): `precio = 9.99`
- **Cadenas** (`str`): `nombre = "Pablo"`
- **Booleanos** (`bool`): `activo = True`

Nombres válidos: `nombre_usuario`, `edad2`, `_precio`
Nombres inválidos: `2nombre` (empieza con número), `mi-variable` (tiene guión), `class` (palabra reservada)

## 2. Diferencia entre = y ==

- `=` asignación: guarda un valor en una variable. Ejemplo: `edad = 20`
- `==` comparación: verifica si dos valores son iguales, devuelve True o False. Ejemplo: `edad == 18` devuelve False

## 3. Indentación en Python

La indentación define los bloques de código. Sin ella el programa no corre y lanza IndentationError.

Ejemplo correcto:
if edad >= 18:
    print("Mayor de edad")
print("Esto siempre se ejecuta")

## 4. Ciclo for vs while

- **for**: cuando sabes cuántas veces repetir
  Ejemplo: `for i in range(5): print(i)`

- **while**: cuando repites hasta que se cumpla una condición
  Ejemplo: `while continuar: opcion = input("Elige: ")`

Usa **for** para recorrer listas o rangos conocidos, **while** para condiciones dinámicas.

## 5. Función range()

Genera una secuencia de números:
- `range(5)` genera 0, 1, 2, 3, 4
- `range(1, 10)` genera 1, 2, 3, 4, 5, 6, 7, 8, 9
- `range(0, 10, 2)` genera 0, 2, 4, 6, 8 (saltos de 2 en 2)