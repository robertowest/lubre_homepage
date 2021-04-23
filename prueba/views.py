import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, QueryDict
from django.http.response import JsonResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic

from django_filters.views import FilterView
from django_tables2 import RequestConfig
from django_tables2.views import SingleTableMixin
from django_tables2.paginators import LazyPaginator

from apps.persona import filters, forms, models, tables
from apps.empresa.models import Comercial

from apps.comunes.utils import PagedFilteredTableView

# asociar persona con comunicación
from apps.comunes.models import Comunicacion
from apps.comunes.filters import ComunicacionFindFilter
from apps.comunes.tables import ComunicacionFindTable
from apps.comunes.forms.comunicacion import ComunicacionForm, ComunicacionFilterFormModal

# asociar persona con domicilio
from apps.comunes.models import Domicilio
from apps.comunes.filters import DomicilioFindFilter
from apps.comunes.tables import DomicilioFindTable
from apps.comunes.forms.domicilio import DomicilioForm, DomicilioFilterFormModal


class PersonaDetailView(PermissionRequiredMixin, generic.DetailView):
    permission_required = 'persona.view_persona'
    model = models.Persona
    template_name = 'prueba/detalle.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comunicaciones'] = context['persona'].comunicaciones.filter(active=True)
        # ajax_cargar_modal(self.request, 'comunicacion', context)
        return context


def ajax_cargar_filtro(request):
    if request.GET['app'] == 'comunicacion':
        filter = ComunicacionFindFilter(request.GET, queryset=Comunicacion.objects.all())
        filter.form.helper = ComunicacionFilterFormModal()
    elif request.GET['app'] == 'domicilio':
        filter = DomicilioFindFilter(request.GET, queryset=Domicilio.objects.all())
        filter.form.helper = DomicilioFilterFormModal()
    return render(request, 'prueba/includes/_modal_find_form.html', { 'filter': filter })

def ajax_cargar_tabla(request):
    if request.GET['app'] == 'comunicacion':
        filter = ComunicacionFindFilter(request.GET, queryset=Comunicacion.objects.all())
        filter.form.helper = ComunicacionFilterFormModal()
        table = ComunicacionFindTable(filter.qs[:5])   # solo 10 registros
    elif request.GET['app'] == 'domicilio':
        filter = DomicilioFindFilter(request.GET, queryset=Domicilio.objects.all())
        filter.form.helper = DomicilioFilterFormModal()
        table = DomicilioFindTable(filter.qs[:5])   # solo 10 registros
    RequestConfig(request).configure(table)
    return render(request, 'prueba/includes/_modal_find_table.html', { 'table': table })

def ajax_asociar_elementos(request):
    if request.GET['app'] == 'comunicacion':
        persona = models.Persona.objects.get(id=request.GET['pk'])
        comunicacion = Comunicacion.objects.get(id=request.GET['fk'])
        persona.comunicaciones.add(comunicacion)
        persona.save()
    elif request.GET['app'] == 'domicilio':
        persona = models.Persona.objects.get(id=request.GET['pk'])
        persona.domicilio = Domicilio.objects.get(id=request.GET['fk'])
        persona.save()
    # return JsonResponse({'result': True}, status=200)
    return HttpResponseRedirect(reverse('prueba:detail', args=[persona.pk]))
