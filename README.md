# lubre_homepage

Reemplazo de la homepage de Lubre SRL utilizando Django 2.1.15


## Pantallazos

![Home Page](pantalla.png)


## Instalación de Firebird

El instalador de django-firebird es antiguo y no funciona con la versión 2.5 por lo que habrá que instalarlo manualmente (# django-firebird==2.0 #)

Primero realizamos la instalación standar de firebird y el módulo para django
```
pip install fdb
pip install django-firebird
```

Ahora nos toca actualizar el módulo instalado con la nueva versión, pero lo haremos desde el código fuente. 
Nos posicionamos en la carpeta donde bajaremos el código fuente: 
```
git clone git://github.com/maxirobaina/django-firebird.git
cd django-firebird
```

Activamos el entorno virtual que afecta al proyecto e instalamos el módulo python
```
source [path]/.env/bin/activate
python setup.py install
```

Ahora (dependiendo de la versión de python) tendremos en nuestra carpeta de módulos el correspondiente a la nueva versión de firebird
[path]/.env/lib/pythonX/site-packages/django_firebird-2.XaX-pyX.X.egg

Creamos un enlace a nuestra carpeta firebird

cd [path]/.env/lib/pythonX/site-packages/django/db/backends
ln -s [path]/.env/lib/pythonX/site-packages/django_firebird-2.XaX-pyX.X.egg/firebird

con esto ya tendremos nuestro backend. Yo tuve un error relacionado con _RemovedInDjango21Warning_ que lo solucioné de la siguiente manera:

modificar el archivo _introspection.py_

nano [path]/.env/lib/pythonX/site-packages/django/db/backends/firebird/introspection.py

Comentamos la línea 6
```
# from django.utils.deprecation import RemovedInDjango21Warning
```

Reemplazamos la línea 154
```
       warnings.warn(
            "get_indexes() is deprecated in favor of get_constraints().",
            RemovedInDjango21Warning, stacklevel=2
        )
```

por esta
```
        warnings.warn("get_indexes() is deprecated in favor of get_constraints().")
```


Probamos si funciona la conexión:
```
$ python manage.py shell

from django.db import connections
from django.db.utils import OperationalError
db_conn = connections['firebird']
try:
    c = db_conn.cursor()
    print('conexión correcta')
except OperationalError:
    print('error de conexión')
else:
    connected = True
```


## Instalación de MySQL
```
sudo apt-get install python3-dev python3-mysqldb libmysqlclient-dev libmariadbclient-dev
sudo apt-get install mariadb-client
pip install mysqlclient
```