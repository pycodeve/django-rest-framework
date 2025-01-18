# Pasos previos
> mkdir store_app
> cd store_app
> python -m venv vienv or virtualenv vienv

## In cmd.exe (Windows)
> vienv\Scripts\activate.bat

## In PowerShell (Windows)
> vienv\Scripts\Activate.ps1

## Linux
> source ./vienv/Scripts/activate

# Creando un proyecto

## Instalando primeras dependencias
> pip install django
> pip install djangorestframework

## Creando el archivo requirements.txt
> pip freeze > requirements.txt

## Creando un proyecto
> django-admin startproject store .

## Agregar rest_framework al archivo settings

INSTALLED_APPS = [
    ...
    'rest_framework',
]

## Creando las apps

> python manage.py startapp products
> python manage.py startapp suppliers
> python manage.py startapp coupons

## Agregar las apps al archivo settings

INSTALLED_APPS = [
    ...
    'rest_framework',
    'products',
    'suppliers',
    'coupons',
]

# Arrancar proyecto
> python manage.py runserver