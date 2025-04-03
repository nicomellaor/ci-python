# Proyecto de Integración
Integración Continua (CI) con Python y GitHub Actions.

## Instalación y configuración
### 1) Clonar el repositorio
   
`git clone https://github.com/nicomellaor/proyecto-integracion.git`

`cd proyecto-integracion`

### 2) Crear entorno virtual

`python -m venv venv`

`source venv/bin/activate` (Linux)

`source venv/Scripts/activate` (Windows)

### 3) Instalar Dependencias

`pip install -r requirements.txt`

### 4) Ejecución de Pruebas en local

`python -m unittest tests`

### 5) CI con GitHub Actions

Este proyecto usa GitHub Actions para ejecutar automáticamente las pruebas cuando se hace un push.

`.github/workflows/ci.yml`: archivo que define el flujo del CI.
