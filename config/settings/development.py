"""
Configuraciones para entorno de desarrollo
./manage.py runserver --settings=config.settings.development
"""

import os
from config.settings.base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# host permitidos
ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# quitamos todas las restricciones para las claves de usuarios
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
]   


# archivos estáticos
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
MEDIA_URL  = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# traducciones
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale'),]


# para que funcione el proceso de registro de usuarios
# esto evitará que se envíe un email e imprimirá el resultado por la consola
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = os.path.join(BASE_DIR, "static/sent_emails")


# configuración para debug
INSTALLED_APPS += ['debug_toolbar',]
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',]
INTERNAL_IPS = ['localhost', '127.0.0.1', '172.19.0.1']  # gateway del docker


