# Guía de Instalación y Configuración del Proyecto

Este proyecto está construido con **Python 3.14** y **Django 6.1.1**.

---

## Requisitos Previos

* **Python 3.14+** (Verifica con `python --version` o `python3 --version`)
* **PostgreSQL (psql)** *(Opcional si decides usar SQLite)*

---

## Configuración del Ambiente Virtual


### 1. Crear el ambiente virtual
```bash
# En Linux/macOS
python3 -m venv venv

# En Windows
python -m venv venv
```

### 2. Activar el ambiente virtual
```bash
# En Linux/macOS
source venv/bin/activate

# En Windows (Command Prompt)
venv\Scripts\activate.bat

# En Windows (PowerShell)
.\venv\Scripts\Activate.ps1
```

---

## Instalación de Dependencias

```bash
pip install -r requirements.txt
```
---

## 🗄️ Configuración de la Base de Datos

Puedes elegir entre **SQLite** (recomendado para desarrollo rápido y pruebas) o **PostgreSQL** (recomendado para entornos más avanzados).

Edita el archivo `tu_proyecto/settings.py` según el motor de base de datos que prefieras usar:

### 🔹 Opción 1: postgres (Por defecto)

Necesitarás crear una base de datos en postgres llamada hito3, caso contrario, revisa el archivo /proyecto-inmueble/settings.py y copia esto donde dice DATABASES

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```


## Migraciones, Superusuario y Fixtures

Una vez configurada la base de datos, ejecuta las migraciones correspondientes e instala los datos iniciales.

### 1. Aplicar migraciones base
```bash
python manage.py migrate
```

### 2. Crear un Superusuario
Crea una cuenta con privilegios de administrador para ingresar al panel de Django (`/admin`):

```bash
python manage.py createsuperuser
```
> Sigue las instrucciones en pantalla para ingresar el nombre de usuario, correo y contraseña.

### 3. Cargar Fixtures (Datos Iniciales)
debes cargar las fixtures en el siguiente orden

```bash
python manage.py loaddata regiones.json
python manage.py loaddata comunas.json
python manage.py loaddata tipo_inmuebles.json
python manage.py loaddata usuario.json
python manage.py loaddata inmuebles.json
```

---

## Ejecutar el Servidor de Desarrollo

con todo lo anterior listo, ya puedes correr el servidor de manera local =)

```bash
python manage.py runserver
```
Abre tu navegador e ingresa a `http://127.0.0.1:8000/`. ¡Listo para jugar :D
