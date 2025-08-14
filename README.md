# API RESTful de Gestión de Tareas (To-Do List)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Django REST Framework](https://img.shields.io/badge/DRF-A5B203?style=for-the-badge&logo=django-rest-framework&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=json-web-tokens&logoColor=white)

---

## Descripción del Proyecto

Esta es una **API RESTful** 
para gestionar tareas personales, desarrollada con Django y Django REST Framework.
Permite a los usuarios registrarse, autenticarse con tokens JWT y gestionar sus propias listas de tareas
de forma segura.

---

## Características Principales

-   **Autenticación segura:** Implementación de JWT (JSON Web Tokens) para el acceso a la API.
-   **Autorización por usuario:** Cada usuario solo puede ver y gestionar sus propias tareas.
-   **API CRUD completa:** Funcionalidades para Crear, Leer, Actualizar y Eliminar tareas.
-   **Validación de datos:** Serializadores que garantizan la integridad de los datos.

---

## Tecnologías Utilizadas

-   **Backend:** Python 3.10
-   **Framework:** Django 5.x
-   **API:** Django REST Framework
-   **Autenticación:** djangorestframework-simplejwt
-   **Base de datos:** PostgreSQL / SQLite

---

## Instalación y Configuración

Sigue estos pasos para poner en marcha el proyecto en tu máquina local.

**1. Clonar el repositorio:**
git clone https://github.com/Janzam/API-RESTful-para-gesti-n-de-tareas-To-Do-List-.git
cd API-RESTful-para-gesti-n-de-tareas-To-Do-List-


**2Crear un entorno virtual e instalar dependencias:**

python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
pip install -r requirements.txt
**3. Configurar la base de datos y migraciones:**
python manage.py makemigrations
python manage.py migrate

**4. Crear un superusuario (opcional pero recomendado):**

python manage.py createsuperuser
**5. Ejecutar el servidor:**
python manage.py runserver

**Rutas**
/api/tasks/  #crea tareas
/api/tasks/[id]  #elimina por id o las modifica 
/login/  
 

