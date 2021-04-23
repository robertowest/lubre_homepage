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


# Create your views here.
def home(request):
    # return render(request, 'base.html', context={},)
    return render(request, 'ejemplos/register.html', context={},)


class PersonaTemplateView(generic.TemplateView):
    # si no existe página index llamamos a otra función
    def get(self, request, *args, **kwargs):
        return PersonasListView.as_view()(request)


class PersonasListView(LoginRequiredMixin, PagedFilteredTableView):
    model = models.Persona
    table_class = tables.PersonaTable
    filter_class = filters.PersonaFilter
    formhelper_class = forms.PersonaFilterForm
    template_name = 'comunes/tabla2.html'

    def get_queryset(self):
        # # eliminamos las personas que son comerciales de la empresa
        # inner_qs = Comercial.objects.all()
        # obj_list = models.Persona.objects.exclude(id__in=inner_qs) \
        #                 .filter(active=True).order_by('nombre', 'apellido')
        # return obj_list
        return models.Persona.objects.filter(active=True)


class PersonaCreateView(PermissionRequiredMixin, generic.CreateView):
    # permission_required = '{domain}/add_{app}'.format(domain='persona', app='persona')
    permission_required = 'persona.add_persona'

    model = models.Persona
    form_class = forms.PersonaForm
    template_name = 'comunes/formulario.html'
    form_title = 'Nueva Persona'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = self.form_title
        return context
        
    def form_valid(self, form):
        response = super().form_valid(form)
        # terminamos, ¿hacia dónde vamos?
        if 'previous_url' in self.request._post:
            return HttpResponseRedirect(self.request._post['previous_url'])
        return response


class PersonaDetailView(PermissionRequiredMixin, generic.DetailView):
    permission_required = 'persona.view_persona'
    model = models.Persona
    # template_name = 'comunes/detalle.html'
    template_name = '{app}/detalle.html'.format(app=model._meta.verbose_name.lower())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comunicaciones'] = context['persona'].comunicaciones.filter(active=True)
        return context


class PersonaUpdateView(PermissionRequiredMixin, generic.UpdateView):
    permission_required = ['persona.add_persona', 'persona.change_persona']
    model = models.Persona
    form_class = forms.PersonaForm
    template_name = 'comunes/formulario.html'
    form_title = 'Modificación de Persona'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = self.form_title
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        # terminamos, ¿hacia dónde vamos?
        if 'previous_url' in self.request._post:
            return HttpResponseRedirect(self.request._post['previous_url'])
        return response


class PersonaDeleteView(PermissionRequiredMixin, generic.DeleteView):
    permission_required = 'persona.delete_persona'
    model = models.Persona
    success_message = "Registro eliminado correctamente"

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):    
        redirect = self.request.GET.get('next')
        if redirect:
            return redirect
        return reverse_lazy('persona:list')


# -----------------------------------------------------------------------------
# crear contactos asociados
# -----------------------------------------------------------------------------

class CreateContactView(PermissionRequiredMixin, generic.CreateView):
    permission_required = 'comunes.add_comunicacion'

    model = Comunicacion
    form_class = ComunicacionForm
    template_name = 'comunes/formulario.html'
    form_title = 'Nueva Comunicación'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = self.form_title
        return context

    def form_valid(self, form):
        response = super().form_valid(form)

        # grabamos el objeto para obtener identificador
        self.object = form.save()
        # obtenemos el objeto primario
        persona = models.Persona.objects.get(id=self.kwargs['fk'])
        # creamos la asociación
        persona.comunicaciones.add(self.object)

        # terminamos, ¿hacia dónde vamos?
        if 'previous_url' in self.request._post:
            return HttpResponseRedirect(self.request._post['previous_url'])
        return response

# -----------------------------------------------------------------------------
# crear direcciones asociadas
# -----------------------------------------------------------------------------

class CreateAddressView(PermissionRequiredMixin, generic.CreateView):
    permission_required = 'comunes.add_domicilio'

    model = Domicilio
    form_class = DomicilioForm
    template_name = 'comunes/formulario.html'
    form_title = 'Nuevo Domicilio'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = self.form_title
        return context

    def form_valid(self, form):
        response = super().form_valid(form)

        # grabamos el objeto para obtener identificador
        self.object = form.save()
        # obtenemos el objeto primario
        persona = models.Persona.objects.get(id=self.kwargs['fk'])
        # creamos la asociación
        persona.domicilio = self.object
        persona.save()

        # terminamos, ¿hacia dónde vamos?
        if 'previous_url' in self.request._post:
            return HttpResponseRedirect(self.request._post['previous_url'])
        return response

# -----------------------------------------------------------------------------
# eliminación de elementos asociados
# -----------------------------------------------------------------------------

@login_required(login_url='/accounts/login/')
def persona_contacto_eliminar(request, pk, fk):
    p = models.Persona.objects.get(id=pk)
    p.comunicaciones.remove(fk)
    url = reverse('persona:detail', args=(), kwargs={'pk': pk})
    return HttpResponseRedirect(url)

# -----------------------------------------------------------------------------
# asociar elementos
# -----------------------------------------------------------------------------

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
