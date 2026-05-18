# Investigación: Buenas Prácticas y Comandos Avanzados

## 1. Git Rebase vs Git Merge

- **Merge**: une dos ramas creando un commit de fusión, conservando el historial completo
- **Rebase**: reaplica los commits de una rama sobre otra, creando un historial lineal

**Cuándo usar rebase**: en ramas personales antes de hacer PR para tener historial limpio.
"Reescribir la historia" significa modificar commits ya existentes, cambiando sus hashes.

## 2. Git Stash

Guarda temporalmente cambios sin hacer commit, para poder cambiar de rama sin perderlos.

**Ejemplo**: estás trabajando en una feature y necesitas urgente cambiar a main para un fix.
```bash
git stash        # guarda los cambios
git checkout main
# haces el fix...
git checkout mi-rama
git stash pop    # recupera los cambios guardados
## 3. Conventional Commits

Convención estándar para mensajes de commit que facilita generar changelogs automáticos.

Es importante porque hace el historial legible y permite automatización.

Prefijos adicionales:
- `chore:` — tareas de mantenimiento (actualizar dependencias)
- `perf:` — mejoras de rendimiento
- `ci:` — cambios en integración continua

## 4. Git Flow

Modelo de branching con ramas especializadas para proyectos grandes.

Tipos de ramas:
- `main` — código en producción
- `develop` — integración de features
- `feature/` — nuevas funcionalidades
- `release/` — preparación de versiones
- `hotfix/` — correcciones urgentes en producción

## 5. HEAD Detached

Ocurre cuando checkout apunta a un commit específico en vez de a una rama.

Para salir: `git checkout main`

## 6. Git Log

Muestra el historial de commits del repositorio.

Flags útiles:
- `git log --oneline` — muestra cada commit en una línea
- `git log --graph` — muestra el árbol de ramas visualmente
- `git log --author="nombre"` — filtra commits por autor

Ejemplo: `git log --oneline --graph --all`