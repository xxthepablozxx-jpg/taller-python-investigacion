# Investigación Git Básico

## 1. ¿Qué es el Staging Area?

El **staging area** (o índice) es una zona intermedia donde se preparan los cambios antes de hacer un commit.

- **Working Directory**: donde editas los archivos localmente
- **Staging Area**: donde seleccionas qué cambios incluir en el próximo commit (`git add`)
- **Repository**: donde se guardan los commits definitivamente (`git commit`)

Es útil porque permite elegir exactamente qué cambios incluir en cada commit, sin tener que guardar todo a la vez.

## 2. ¿Qué hace git status?

Muestra el estado actual del repositorio. Información que proporciona:
1. En qué rama estás actualmente
2. Archivos modificados que aún no están en staging
3. Archivos en staging listos para commit
4. Archivos sin seguimiento (untracked)

## 3. Diferencia entre git fetch y git pull

- **git fetch**: descarga los cambios remotos pero NO los aplica al working directory
- **git pull**: descarga Y aplica los cambios automáticamente (fetch + merge)

`git fetch` es más seguro porque puedes revisar los cambios antes de aplicarlos.

## 4. ¿Qué es un Merge Conflict?

Ocurre cuando dos ramas modifican la misma línea de un archivo y Git no puede decidir cuál versión conservar.

**Ejemplo**: la rama `desarrollo` y `main` modifican la misma línea del README.

**Pasos para resolverlo**:
1. `git merge rama` — Git marca los conflictos
2. Abrir el archivo y elegir qué versión conservar
3. `git add archivo`
4. `git commit`