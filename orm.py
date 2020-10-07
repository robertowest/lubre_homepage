#!/home/roberto/miniconda3/envs/lubresrl/bin/python

import os, sys
# sys.path.append('/var/www/lubresrl.com.ar/')
# os.environ['DJANGO_SETTINGS_MODULE'] = 'config.custom'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.custom')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from apps.empresa.models import Empresa
from ORM.models import Clientes


def buscar_modificaciones():
    """
    busca empresas que hayan sido modificadas para impactar en la base de datos 
    del sistema de gestión
    """

    # num="0123456789"
    # print("("+num[:3]+") "+num[3:6]+"-"+num[6:])
    # '(012) 345-6789'
    # print( c[:2]+"-"+c[2:10]+"-"+c[-2:-1])

    # recuperar todos los registros con el campo impactar=True
    empresas = Empresa.objects.filter(impactar=True)
    for empresa in empresas:
        if empresa.referencia_id:
            print("Actulización de datos de la empresa: %s" % empresa)
            cliente = Clientes.objects.using('firebird').get(idcliente=empresa.referencia_id)
            if cliente:
                print("Nombre de fantasía: %s --> %s" % (cliente.fantasia, empresa.nombre))
                print("Razón social      : %s --> %s" % (cliente.nombre, empresa.razon_social))
                cuit = empresa.cuit[:2] + "-" + empresa.cuit[2:10] + "-" + empresa.cuit[-2:-1]
                print("CUIT              : %s --> %s" % (cliente.cuit, cuit))

                try:
                    cliente.fantasia = empresa.nombre.upper()
                    cliente.nombre = empresa.razon_social.upper()
                    cliente.cuit = cuit
                    cliente.save()
                    # empresa.impactar = False
                    # empresa.save()
                except:
                    print('Error al intentar actualizar los datos del cliente: ' + empresa)

        else:
            print("Alta de la empresa: %s" % empresa)


if __name__ == "__main__":
    buscar_modificaciones()
