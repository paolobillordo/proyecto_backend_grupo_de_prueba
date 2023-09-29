# proyecto_backend_grupo_de_prueba
Backend para el proyecto de programación 2
Tal como lo pedía el TIF desarrollamos 2 repositorios en GitHub, este es el repositorio del backend
Lo desarrolamos siguien el patron MVC

estas son las librerias necesarias para que funcione el servidor

Babel                  2.12.1
blinker                1.6.2
certifi                2023.7.22
charset-normalizer     3.2.0
click                  8.1.6
colorama               0.4.6
Flask                  2.3.2
Flask-Cors             4.0.0
idna                   3.4
itsdangerous           2.1.2
Jinja2                 3.1.2
MarkupSafe             2.1.3
mysql-connector-python 8.0.33
numpy                  1.25.1
pip                    23.2.1
protobuf               3.20.3
python-decouple        3.8
python-dotenv          1.0.0
requests               2.31.0
setuptools             65.5.0
tkcalendar             1.6.1
urllib3                2.0.4
Werkzeug               2.3.6

Tambien tiene crear un archivo .env con  las siguientes variables de entorno:

SECRET_KEY = 352528b35a4cca7bf961c3f7c0dac9642c527428388d4de5f443df34f0e6e320
DATABASE_USERNAME = 'root'
DATABASE_PASSWORD = 'MoxOz0dFgb7VaTMDhFEi'
DATABASE_HOST = 'containers-us-west-80.railway.app'
DATABASE_PORT = '6553'

Entendemos que esto es inseguro pero a fines del TIF es la manera de pasarle las credenciales
