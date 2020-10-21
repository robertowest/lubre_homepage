#!/home/roberto/miniconda3/envs/lubresrl/bin/python

import os, sys

FILE = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(FILE))

sys.path.append(BASE_DIR)     # '/var/www/lubresrl.com.ar/'
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.custom'
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.custom')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from apps.comunes.models import Domicilio
from apps.empresa.models import Empresa
from ORM.models import Clientes


def buscar_modificaciones():
    """
    busca empresas que hayan sido modificadas para impactar en la base de datos 
    del sistema de gestión
    """

    # recuperar todos los registros con el campo impactar=True
    empresas = Empresa.objects.filter(impactar=True)
    for empresa in empresas:
        if empresa.referencia_id:
            cliente = Clientes.objects.using('firebird').get(idcliente=empresa.referencia_id)
            if cliente:
                # print("Nombre de fantasía: %s" % cliente.fantasia)
                # print("    cambiar por --> %s" % empresa.nombre)
                # print("Razón social      : %s" % cliente.nombre)
                # print("    cambiar por --> %s" % empresa.razon_social)
                # print("CUIT              : %s" % cliente.cuit)
                # cuit = empresa.cuit[:2] + "-" + empresa.cuit[2:10] + "-" + empresa.cuit[-1:]
                # print("    cambiar por --> %s" % cuit)

                try:
                    actualizar_cliente(empresa, cliente)
                    actualizar_contacto(empresa, cliente)
                    actualizar_domicilio(empresa, cliente)
                    cliente.save()
                    # empresa.impactar = False
                    # empresa.save()
                except Exception as err:
                    print('Error al actualizar los datos del cliente: ', empresa.referencia_id)
                    print(err)
        else:
            try:
                cliente = nuevo_cliente(empresa)
                cliente.save(using='firebird')
                empresa.referencia_id = cliente.idcliente
                # empresa.impactar = False
                empresa.save()
            except Exception as err:
                print('Error al crear el cliente: ', empresa.nombre)
                print(err)


def formato_cuit(texto):
    cuit = texto.replace("-", "")
    return cuit[:2] + "-" + cuit[2:10] + "-" + cuit[-1:]


def actualizar_cliente(empresa, cliente):
    cliente.fantasia = empresa.nombre[:60].upper()
    cliente.nombre = empresa.razon_social[:60].upper()
    cliente.cuit = formato_cuit(empresa.cuit)
    cliente.bloqueado = ['S','N'][empresa.active]


def actualizar_contacto(empresa, cliente):
    telefono = False
    correo = False
    comunicaciones = empresa.comunicaciones.select_related('tipo')

    for reg in comunicaciones:
        if reg.tipo_id == 3 and not telefono:
            cliente.telef_d = reg.texto
            telefono = True

        elif reg.tipo_id == 6 and not correo:
            cliente.email_d = reg.texto
            correo = True


def actualizar_domicilio(empresa, cliente):
    sql = "SELECT d.* " + \
          "FROM empresa e " + \
          "LEFT JOIN empresa_actividades ea ON ea.empresa_id = e.id " + \
          "LEFT JOIN empresa_actividad_domicilios ead ON ead.empresa_actividad_id = ea.id " + \
          "LEFT JOIN domicilio d ON d.id = ead.domicilio_id and d.tipo_id = 1 " + \
          "WHERE e.id = %s " % empresa.id
    domicilios = Domicilio.objects.raw(sql)

    # sin importar cuantos domicilios fiscales obtenemos, solo tomaremos el primero    
    if domicilios:
        cliente.direc_d = '{} {} {}'.format(domicilios[0].get_tipo_calle_display(), 
                                            domicilios[0].nombre,
                                            domicilios[0].numero)[:60]
        if (domicilios[0].provincia.nombre == 'Tucumán'):
            cliente.idprovincia = 'T'
        cliente.localidad = domicilios[0].localidad.nombre[:60]
        cliente.direccion = domicilios[0].departamento.nombre[:60]


def nuevo_cliente(empresa):
    cliente = Clientes()

    cliente.idcliente = empresa.id
    cliente.idactividad = 330     # lubricentro
    cliente.idcalifica = 1        # activo
    cliente.idestadocliente = 0   # normal
    cliente.idformacobro = 15     # 15 días fecha factura
    cliente.idlista = 1           # lista de precios base
    cliente.idtipimun = "E"       # exento
    cliente.idtipodoc = 80        # cuit
    cliente.idtipoingbruto = "E"  # exento
    cliente.idtipoiva = "I"       # responsable inscripto
    cliente.iva = "N"             # n

    # cliente.idcli_nivel1 = 2    
    # cliente.idcli_nivel2 = 3    
    # cliente.idplan = 16         

    actualizar_cliente(empresa, cliente)
    actualizar_contacto(empresa, cliente)
    actualizar_domicilio(empresa, cliente)

    return cliente


if __name__ == "__main__":
    buscar_modificaciones()
