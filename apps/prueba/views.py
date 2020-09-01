from django.shortcuts import render

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

from apps.persona.models import Persona
from apps.empresa.models import Comercial
from .filters import ComercialFilter
from .tables import ComercialTable

def index(request):
    return render(request, 'prueba/abc.html')


def busqueda_modal(request):
    obj_list = Comercial.objects.filter(active=True).order_by('persona')
    return render(request, 'prueba/busqueda_modal.html', {'object_list': obj_list})


def busqueda_table_modal(request):
    obj_list = Comercial.objects.filter(active=True).order_by('persona')
    context = {
        'tableID': 'dataTableModal',
        'object_list': obj_list,
    }
    return render(request, 'prueba/busqueda_table_modal.html', context)


def comercial_search(request):
    obj_list = Comercial.objects.filter(active=True).order_by('persona')
    obj_filter = ComercialFilter(request.GET, queryset=obj_list)
    return render(request, 'prueba/comercial_search.html', {'filter': obj_filter})


class comercial_search_2(SingleTableMixin, FilterView):
    model = Comercial
    table_class = ComercialTable
    filterset_class = ComercialFilter
    template_name = 'prueba/comercial_search_2.html'


def comercial_search_3(request):
    obj_list = Comercial.objects.filter(active=True).order_by('persona')
    obj_filter = ComercialFilter(request.GET, queryset=obj_list)
    context = {
        'filter': obj_filter,
        'table': obj_list
    }
    return render(request, 'prueba/comercial_search_3.html', context)


# from django.views.generic import TemplateView
#
# class resultado(TemplateView):
#     # return render(request, 'prueba/resultado.html')
#     template_name = 'prueba/resultado.html'
def resultado(request, pk):
    return render(request, 'prueba/resultado.html', {'seleccion': pk})




def companyListView(request):
    context = {}
    object_list = Comercial.objects.filter(active=True).order_by('persona')
    if request.method == 'POST' and request.is_ajax():
        ID = request.POST.objects.get('id')
        object_list = Comercial.get(id=ID)  # So we send the company instance
        context['object_list'] = object_list
    context['object_list'] = object_list
    return render(request, 'prueba/prueba1.html', context)



from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django_tables2.paginators import LazyPaginator
from apps.persona.filters import PersonaFilter
from apps.persona.tables import PersonaTable

class tablaListView(LoginRequiredMixin, SingleTableMixin, FilterView):
    table_class = PersonaTable
    filterset_class = PersonaFilter
    template_name = 'persona/tabla.html'
    # ordering = ['nombre', 'apellido', 'id']
    # paginator_class = LazyPaginator
