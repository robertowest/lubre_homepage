"""
Configuraciones para entorno de desarrollo
./manage.py runserver --settings=config.settings.development
"""

import os
from config.settings import *
from decouple import config, Csv


# -------------------------------------------------------------------
# SECURITY WARNING: don't run with debug turned on in production!
# -------------------------------------------------------------------
# os.environ.get('DJANGO_DEBUG', True)
DEBUG = config('DJANGO_DEBUG', default=True, cast=bool)
if DEBUG:
    ENV = config('DJANGO_ENVIRONMENT', default='DEV')
else:
    ENV = config('DJANGO_ENVIRONMENT', default='PROD')


# -------------------------------------------------------------------
# host permitidos
# -------------------------------------------------------------------
# os.environ.get('DJANGO_ALLOWED_HOSTS', '*').split()
# ALLOWED_HOSTS = ['190.105.227.83']
# ALLOWED_HOSTS = config('DJANGO_ALLOWED_HOSTS', default='*', cast=Csv())
# ALLOWED_HOSTS = config('DJANGO_ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])
ALLOWED_HOSTS = config('DJANGO_ALLOWED_HOSTS', default='*', cast=Csv())


# -------------------------------------------------------------------
# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
# -------------------------------------------------------------------
DATABASES = {
    'development': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },    
    'test': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'carteralubre',
        'HOST': '172.17.0.2',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': 'roberto',
    },
    'production': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'homepage_dj',
        'HOST': '190.105.227.83',
        'PORT': '3306',
        'USER': 'django',
        'PASSWORD': 'django',
    },
    'firebird': {
        # lubresrl.dyndns.org:4310
        'ENGINE': 'django.db.backends.firebird',
        'NAME': 'P:\\PRUEBA\\DATOS\\GESTION.FDB',
        'USER': 'SYSDBA',
        'PASSWORD': 'masterkey',
        'HOST': 'lubresrl.dyndns.org',
        'PORT': '3050',
        'OPTIONS': {'charset': 'ISO8859_1'}
    },
}
if ENV == 'PROD':
    DATABASES['default'] = DATABASES['production']
elif ENV == 'TEST':
    DATABASES['default'] = DATABASES['test']
else:
    DATABASES['default'] = DATABASES['development']

# # para utilizar migration
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'carteralubre',
#         'HOST': '172.17.0.2',
#         'PORT': '3306',
#         'USER': 'root',
#         'PASSWORD': 'roberto',
#     },
# }


# -------------------------------------------------------------------
# restricciones para las claves de usuarios
# -------------------------------------------------------------------
if ENV == 'DEV':
    AUTH_PASSWORD_VALIDATORS = [
        {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    ]
else:
    AUTH_PASSWORD_VALIDATORS = [
        {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
        {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
        {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
        {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
    ]


# -------------------------------------------------------------------
# ubicación de los templates públicos
# -------------------------------------------------------------------
TEMPLATES[0]['DIRS'] = [os.path.join(BASE_DIR, "templates"),]


# -------------------------------------------------------------------
# archivos estáticos
# -------------------------------------------------------------------
if DEBUG:
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL  = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# -------------------------------------------------------------------
# traducciones
# -------------------------------------------------------------------
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale'),]


# -------------------------------------------------------------------
# para que funcione el proceso de registro de usuarios
# esto evitará que se envíe un email e imprimirá el resultado por la consola
# -------------------------------------------------------------------
if ENV == 'DEV':
    EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
    EMAIL_FILE_PATH = os.path.join(BASE_DIR, "static/sent_emails")
else:
    EMAIL_HOST = config('DJANGO_EMAIL_HOST', default='localhost')
    EMAIL_PORT = config('DJANGO_EMAIL_PORT', default=25, cast=int)
    EMAIL_HOST_USER = config('DJANGO_EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = config('DJANGO_EMAIL_HOST_PASSWORD')
    EMAIL_USE_SSL = config('DJANGO_EMAIL_USE_SSL', default=False, cast=bool)
    # EMAIL_USE_TLS = config('DJANGO_EMAIL_USE_TLS', default=False, cast=bool)


# -------------------------------------------------------------------
# configuración para debug
# -------------------------------------------------------------------
if DEBUG:
    INSTALLED_APPS += ['debug_toolbar',]
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',]
    INTERNAL_IPS = ['localhost', '127.0.0.1', '172.19.0.1']  # gateway del docker


# -------------------------------------------------------------------
# configuración para django-crispy-forms
# -------------------------------------------------------------------
INSTALLED_APPS += ['crispy_forms',]
CRISPY_TEMPLATE_PACK = 'bootstrap4'


# -------------------------------------------------------------------
# configuración para django-templated-email
# -------------------------------------------------------------------
TEMPLATED_EMAIL_BACKEND = 'templated_email.backends.vanilla_django.TemplateBackend'
TEMPLATED_EMAIL_AUTO_PLAIN = False
TEMPLATED_EMAIL_TEMPLATE_DIR = 'templated_email/'
TEMPLATED_EMAIL_FILE_EXTENSION = 'email'


# -------------------------------------------------------------------
# redirecciona a home al realizar un login exitoso
# -------------------------------------------------------------------
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/accounts/redirect/'
LOGOUT_URL = '/accounts/logout/'
LOGOUT_REDIRECT_URL = '/'
