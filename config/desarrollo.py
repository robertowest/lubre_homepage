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
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'development': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'admin_desarrollo',
        'HOST': '190.105.227.83',  # LatinCloud
        'PORT': '3306',
        'USER': 'admin_roberto',
        'PASSWORD': 'roberto',
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
# esta definición funciona bien pero no funciona con migrate o makemigrations
if ENV == 'PROD':
    DATABASES['default'] = DATABASES['production']
elif ENV == 'TEST':
    DATABASES['default'] = DATABASES['test']
else:
    DATABASES['default'] = DATABASES['development']

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'desarrollo_dj',
    #     'HOST': '192.168.1.2',  # lubre local
    #     'PORT': '3306',
    #     'USER': 'roberto',
    #     'PASSWORD': 'roberto',
    # },
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'admin_desarrollo',
    #     'HOST': '190.105.227.83',  # LatinCloud
    #     'PORT': '3306',
    #     'USER': 'admin_roberto',
    #     'PASSWORD': 'roberto',
    # },
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lubresrl_dj',
        'HOST': '172.17.0.2',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': 'roberto',
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


# -------------------------------------------------------------------
# restricciones para las claves de usuarios
# -------------------------------------------------------------------
if ENV == 'PROD':
    AUTH_PASSWORD_VALIDATORS = [
        {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
        {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
        {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
        {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
    ]
else:
    AUTH_PASSWORD_VALIDATORS = []


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
# redirecciona a home al realizar un login exitoso
# -------------------------------------------------------------------
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/accounts/redirect/'
LOGOUT_URL = '/accounts/logout/'
LOGOUT_REDIRECT_URL = '/'


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
# configuración para django-social-auth
# -------------------------------------------------------------------
AUTHENTICATION_BACKENDS = [
    # 'social_core.backends.google.GoogleOpenId',
    # 'social_core.backends.google.GoogleOAuth2',
    # 'social_core.backends.google.GoogleOAuth',
    # 'social_core.backends.linkedin.LinkedinOAuth2',
    # 'social_core.backends.open_id.OpenIdAuth',
    # 'social_core.backends.twitter.TwitterOAuth',
    # 'social_core.backends.yahoo.YahooOpenId',
    'social_core.backends.instagram.InstagramOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

SOCIAL_AUTH_FACEBOOK_KEY = config('DJANGO_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = config('DJANGO_FACEBOOK_SECRET')
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'user_link']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {'fields': 'id, name, email, picture.type(large), link'}
SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [('name', 'name'), ('email', 'email'), ('picture', 'picture'), ('link', 'profile_url'),]


from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}



INSTALLED_APPS += [
    'django_filters',
    'django_tables2',
    'bootstrap3',
    
    # prueba -------------------------------
    'apps.prueba',
]
