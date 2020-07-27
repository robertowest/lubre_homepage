"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.1.15.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from decouple import config

# /project
#     /apps
#     /config
#         /settings
#             base.py
#     /static
#
# FILE = os.path.abspath(__file__)                         == /project/config/settings/base.py
# os.path.dirname(FILE)                                    == /project/config/settings
# os.path.dirname(os.path.dirname(FILE))                   == /project/config
# os.path.dirname(os.path.dirname(os.path.dirname(FILE)))  == /project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# os.environ.get('DJANGO_SECRET_KEY')
SECRET_KEY = config('DJANGO_SECRET_KEY')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # agregado
    'django_currentuser.middleware.ThreadLocalUserMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # social-auth-app-django
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                # propio
                'apps.homepage.contexts.appname',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

# internalización
LANGUAGE_CODE = config('DJANGO_LANGUAGE_CODE', default='en')
TIME_ZONE = config('DJANGO_TIME_ZONE', default='UTC')

USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

# -------------------------------------------------------------------
# aplicaciones del proyecto
# -------------------------------------------------------------------
INSTALLED_APPS += [
    # aplicaciones de terceros -------------
    'ckeditor',
    'mathfilters',
    'social_django',

    # homepage -----------------------------
    'apps.homepage',
    'apps.equivalencia',
    'apps.accounts',
    'apps.tienda',

    # cartera ------------------------------
    'apps.comunes',
    'apps.empresa',
    'apps.persona',

    # gestion ------------------------------
    'apps.firebird',
]

# modelo de datos de user
# AUTH_USER_MODEL = 'accounts.User'
