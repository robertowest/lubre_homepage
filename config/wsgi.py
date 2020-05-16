"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os, sys

sys.path.append('/var/www/lubresrl.com.ar/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.custom'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
