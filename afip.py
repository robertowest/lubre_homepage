#!/home/roberto/miniconda3/envs/lubresrl/bin/python

import os, sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.custom')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# --------------------------------------------------------------

from django.core.files import File
from django_afip import models

# Create a TaxPayer object:
taxpayer = models.TaxPayer(pk=1, name='test taxpayer', cuit=20329642330, is_sandboxed=True)

# Add the key and certificate files to the TaxPayer:
with open('/home/roberto/Programacion/python/PyAfipWS/cert/reingart.key') as key:
    taxpayer.key.save('test.key', File(key))
with open('/home/roberto/Programacion/python/PyAfipWS/cert/reingart.crt') as crt:
    taxpayer.certificate.save('test.crt', File(crt))

taxpayer.save()

# Load all metadata:
models.populate_all()

# Get the TaxPayer's Point of Sales:
taxpayer.fetch_points_of_sales()
