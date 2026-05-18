"""
Programa: Hola Mundo Interactivo
Descripción: Programa que saluda al usuario y muestra un menú de opciones
Autor: xxthepablozxx-jpg
Fecha: 2026-05-17
"""

# ==========================================
# CONSTANTES DEL PROGRAMA
# ==========================================
NOMBRE_PROGRAMA = "Hola Mundo Interactivo"
VERSION = "1.0"
MAX_INTENTOS = 3
ANIO_ACTUAL = 2026

# ==========================================
# PARTE 1: SALUDO INICIAL
# ==========================================
print("=" * 50)
print(f"  {NOMBRE_PROGRAMA} v{VERSION}")
print("=" * 50)

nombre_usuario = input("¿Cuál es tu nombre? ")

if nombre_usuario == "":
    print("No ingresaste un nombre. Te llamaré 'Usuario'")
    nombre_usuario = "Usuario"
else:
    print(f"¡Hola, {nombre_usuario}! Bienvenido/a al programa.")

# ==========================================
# PARTE 2: PREGUNTAR LA EDAD
# ==========================================
edad_texto = input("¿Cuántos años tienes? ")
edad = int(edad_texto)

if edad < 18:
    print(f"Eres menor de edad, {nombre_usuario}.")
    categoria = "joven"
elif edad >= 18 and edad < 60:
    print(f"Eres adulto, {nombre_usuario}.")
    categoria = "adulto"
else:
    print(f"Eres adulto mayor, {nombre_usuario}.")
    categoria = "adulto mayor"

anio_nacimiento = ANIO_ACTUAL - edad
print(f"Naciste aproximadamente en el año {anio_nacimiento}")

# ==========================================
# PARTE 3: MENÚ DE OPCIONES
# ==========================================
print("=" * 50)
print("MENÚ DE OPCIONES")
print("=" * 50)
print("1. Ver tu información")
print("2. Contar del 1 al 10")
print("3. Tabla de multiplicar")
print("4. Salir")
print("=" * 50)

continuar = True
intentos_fallidos = 0

while continuar:
    opcion = input("\nElige una opción (1-4): ")

    if opcion == "1":
        print(f"\nNombre: {nombre_usuario}")
        print(f"Edad: {edad} años")
        print(f"Categoría: {categoria}")
        print(f"Año de nacimiento: {anio_nacimiento}")
        intentos_fallidos = 0

    elif opcion == "2":
        print("\n--- CONTANDO DEL 1 AL 10 ---")
        for numero in range(1, 11):
            print(f"Número: {numero}")
        intentos_fallidos = 0

    elif opcion == "3":
        numero_tabla = int(input("\n¿De qué número quieres la tabla? "))
        print(f"\n--- TABLA DEL {numero_tabla} ---")
        for i in range(1, 11):
            print(f"{numero_tabla} x {i} = {numero_tabla * i}")
        intentos_fallidos = 0

    elif opcion == "4":
        print(f"\n¡Hasta luego, {nombre_usuario}!")
        continuar = False

    else:
        intentos_fallidos += 1
        print(f"\nOpción inválida. Intento {intentos_fallidos} de {MAX_INTENTOS}")
        if intentos_fallidos >= MAX_INTENTOS:
            print("Demasiados intentos fallidos. Cerrando programa...")
            continuar = False

print("\n" + "=" * 50)
print("PROGRAMA FINALIZADO")
print("=" * 50)