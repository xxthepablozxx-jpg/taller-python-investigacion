# Investigación: GitHub y Colaboración

## 1. ¿Qué es un Pull Request (PR)?

Un PR es una solicitud para fusionar cambios de una rama a otra, permitiendo revisión del código antes de integrarlo.

- **Diferencia con merge directo**: el PR permite revisión, comentarios y aprobación antes de fusionar
- **Ventajas**: control de calidad, historial claro, colaboración organizada

## 2. ¿Qué es un Fork?

Copia completa de un repositorio en tu propia cuenta de GitHub.

- **Fork**: copia en tu cuenta GitHub para contribuir a proyectos ajenos
- **Clone**: copia local en tu computadora para trabajar
- Para contribuir a open source: haces fork, clonas tu fork, haces cambios y abres PR al repo original

## 3. ¿Qué es .gitignore?

Archivo que indica a Git qué archivos ignorar y no subir al repositorio.

Archivos que NO deben subirse en Python:
1. `venv/` — entorno virtual
2. `__pycache__/` — archivos compilados
3. `.env` — variables de entorno con contraseñas
4. `*.pyc` — bytecode de Python
5. `.DS_Store` — archivos del sistema

Sin .gitignore se subirían archivos innecesarios o con información sensible.

## 4. ¿Qué son los Issues?

Herramienta para reportar bugs, sugerir mejoras o planificar tareas en GitHub.

Un buen issue debe tener: título claro, descripción del problema, pasos para reproducirlo y resultado esperado.

Se relacionan con commits usando # más el número, ejemplo: `fix: corregir error #3`

## 5. GitHub Actions

Sistema de automatización integrado en GitHub que ejecuta tareas automáticamente.

Ejemplos:
1. Ejecutar tests automáticamente al hacer push
2. Desplegar la aplicación al fusionar con main