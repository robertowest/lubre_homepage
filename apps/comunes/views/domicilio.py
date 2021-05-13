import json

from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from apps.comunes.models import Domicilio as DomicilioModel
from apps.comunes.forms.domicilio import DomicilioForm, DomicilioFilterFormHelper
from apps.comunes.filters import DomicilioListFilter
from apps.comunes.tables import DomicilioTable
from apps.comunes.utils import PagedFilteredTableView


class DomicilioTemplateView(TemplateView):
    # si no existe página index llamamos a otra función
    def get(self, request, *args, **kwargs):
        return DomicilioListView.as_view()(request)


class DomicilioListView(PagedFilteredTableView):
    model = DomicilioModel
    table_class = DomicilioTable
    filter_class = DomicilioListFilter
    formhelper_class = DomicilioFilterFormHelper 
    template_name = 'comunes/tabla2.html'
 

class DomicilioCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'comunes.add_domicilio'

    model = DomicilioModel
    form_class = DomicilioForm
    template_name = 'comunes/formulario.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        # terminamos, ¿hacia dónde vamos?
        if 'previous_url' in self.request._post:
            return HttpResponseRedirect(self.request._post['previous_url'])
        return response


class DomicilioDetailView(DetailView):
    model = DomicilioModel
    template_name = 'comunes/detalle.html'


class DomicilioUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'comunes.change_domicilio'

    model = DomicilioModel
    form_class = DomicilioForm
    template_name = 'comunes/formulario.html'

    def form_valid(self, form):
        messages.success(self.request, 'Domicilio grabado correctamente')
        response = super().form_valid(form)
        # terminamos, ¿hacia dónde vamos?
        if 'previous_url' in self.request._post:
            return HttpResponseRedirect(self.request._post['previous_url'])
        return response


class DomicilioDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'comunes.delete_domicilio'
    pass


# se reeemplazó con django-smart-selects
# # chained dropdown
# from apps.comunes.models import Provincia, Departamento, Localidad

# def carga_departamentos(request):
#     parent = request.GET['fk']
#     if parent:
#         objetos = Departamento.objects.filter(provincia_id=parent).order_by('nombre')
#     else:
#         objetos = Departamento.objects.filter(provincia_id=0)
#     return render(request, 'domicilio/cargar_dropdown.html', {'object_list': objetos})

# def carga_localidades(request):
#     parent = request.GET['fk']
#     if parent:
#         objetos = Localidad.objects.filter(departamento_id=parent).order_by('nombre')
#     else:
#         objetos = Localidad.objects.filter(departamento_id=0)
#     return render(request, 'domicilio/cargar_dropdown.html', {'object_list': objetos})
