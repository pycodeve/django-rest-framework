# Django Rest Framework (Base)

The purpose of this repository is to have a base project using Django Rest Framework, where you can quickly consult the different functions, classes, and ways to create a Rest API.

## Prerequisite Steps
```bash
mkdir store_app
cd store_app
```

## Creating the Virtual Environment
```bash
python -m venv vienv # or virtualenv vienv
```

## Activating the Environment
### In cmd.exe (Windows)
```bash
vienv\Scripts\activate.bat
```
### In PowerShell (Windows)
```bash
vienv\Scripts\Activate.ps1
```
### In Linux
```bash
source ./vienv/Scripts/activate
```

## Creating and Configuring the Project
### Installing Dependencies
```bash
pip install django
pip install djangorestframework
```

### Creating the requirements.txt File
```bash
pip freeze > requirements.txt
```

### Creating the Project
```bash
django-admin startproject store .
```

### Adding rest_framework to settings.py
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

### Creating the Apps
```bash
python manage.py startapp products
python manage.py startapp suppliers
python manage.py startapp coupons
```

### Adding the Apps to settings.py
```bash
INSTALLED_APPS = [
    ...
    'rest_framework',
    'products',
    'suppliers',
    'coupons',
]
```
### Starting the Project
```bash
python manage.py runserver
```

## Additional commands
### Create migrations
```bash
python manage.py makemigrations
```

### Run the migrations
```bash
python manage.py migrate
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)