from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import generic

from . import models

def Equivalencia(request):
    ypf = {}

    if request.method == 'POST':
        # import pdb; pdb.set_trace()
        # marcaId = request.POST['marca']
        # tipoId = request.POST['tipo']
        prodId = request.POST['producto']
        sql = 'SELECT a.id, a.producto, a.marca, a.tipo, b.producto equivalencia, b.marca equivalencia_marca ' +\
              'FROM equivalencia_equivalencia a ' +\
              'INNER JOIN equivalencia_equivalencia b ON b.id = a.parent_id ' +\
              'WHERE a.id = {0}'
        ypf = models.Equivalencia.objects.raw(sql.format(prodId))[0]

    context = {'marcas': models.Equivalencia.MARCA,
               'tipos': models.Equivalencia.TIPO,
               'producto': ypf}

    return render(request, 'equivalencia/form.html', context)


def cargar_productos_ajax(request):
    # http://lubresrl.com.ar/equivalencia/cargar/productos/ajax/?marcaId=1&tipoId=2
    marcaId = request.GET['marcaId']
    tipoId = request.GET['tipoId']

    # if tipoId == 'None':
    #     sql = 'SELECT id, producto FROM equivalencia_equivalencia WHERE marca={0} ORDER BY producto'
    # else:
    #     sql = 'SELECT id, producto FROM equivalencia_equivalencia WHERE marca={0} and tipo={1} ORDER BY producto'
    # data = models.Equivalencia.objects.raw(sql.format(marcaId, tipoId))

    data = models.Equivalencia.objects.filter(marca=marcaId).order_by('producto')
    if tipoId != 'None':
        data = data.filter(tipo=tipoId)
    return render(request, 'equivalencia/cargar_productos_ajax.html', {'productos': data})


class EquivalenciaDetail(generic.DetailView):
    model = models.Equivalencia
    template_name = 'blog/post_detail.html'
