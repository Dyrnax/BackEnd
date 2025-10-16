inicializacion paso a paso desde 0
(o): obligatorio
(pv): primera vez

git config --global user.name "Marco Calfileo" (o)
git config --global user.email marco.calfileo@gmail.com (o)
pip install virtualenv ó python -m pip install virtualenv (o)
virtualenv ambiente (o)
python -m venv ambiente (venv de python)
.\ambiente\Scripts\activate.ps1 si no deja Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
python.exe -m pip install --upgrade pip (o)
pip install django (o)
django-admin startproject drf (pv)
django-admin startapp primera_app (pv)
pip install mysqlclient (o) 
pip install djangorestframework (o)
pip install python-decouple
pip install iconic
pip install drf_yasg
python manage.py migrate (o)
python manage.py makemigrations (o)
python manage.py migrate (o)
python manage.py loaddata data_tipocategoria.json
python manage.py loaddata data_categoria.json
python manage.py loaddata data_nacionalidades.json
python manage.py loaddata data_comunas.json
python manage.py createsuperuser (o)
Username (leave blank to use 'informatica'): zucar
Email address: zucar@zucar.com         
Password: 1234
Password (again):
python manage.py runserver ruta: http://127.0.0.1:8000/
                                 http://127.0.0.1:8000/admin
                                 http://127.0.0.1:8000/primera_app/


#No trabajo en maquina personal :p
en ".env"
SECRET_KEY = 'django-insecure-rc_#uk5gvzmks*#@)$onq1clgm%8hf4m@w8fb9_i8s8%=*=7t#'
DB_ENGINE = 'django.db.backends.mysql'
DB_NAME = 'bd_backend'
DB_USER = 'root'
DB_PASS = ''
DB_HOST = 'localhost'
DB_PORT = '3306'