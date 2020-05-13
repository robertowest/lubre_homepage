"""
Configuraciones para entorno de producción
./manage.py runserver --settings=config.settings.production
"""

import os
from config.settings.base import *


# desabilitamos la depuración
DEBUG = False


# host permitidos
ALLOWED_HOSTS = ['*']   # ['190.105.227.83', '127.0.0.1']


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'homepage_dj',
        'HOST': '190.105.227.83',
        'PORT': '3306',
        'USER': 'django',
        'PASSWORD': 'django',
    },
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


# archivos estáticos
# ./manage.py collectstatic --settings=config.settings.production
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# traducciones
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale'),]


# para que funcione el proceso de registro de usuarios
# esto evitará que se envíe un email e imprimirá el resultado por la consola
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = os.path.join(BASE_DIR, "static/sent_emails")


# configuración para debug
INSTALLED_APPS += ['debug_toolbar']
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
INTERNAL_IPS = ['localhost', '127.0.0.1', '172.19.0.1']  # gateway del docker


