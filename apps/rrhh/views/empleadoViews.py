from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from django_filters.views import FilterView
from django_tables2 import SingleTableView

from apps.comunes.models import Domicilio, Comunicacion
from apps.rrhh import models
from apps.rrhh.filters import empleadoFilters
from apps.rrhh.forms import empleadoForms
from apps.rrhh.tables import empleadoTables

from apps.comunes.utils import PagedFilteredTableView


class EmpleadoTemplateView(generic.TemplateView):
    # si no existe página index llamamos a otra función
    def get(self, request, *args, **kwargs):
        return EmpleadosListView.as_view()(request)


class EmpleadosListView(LoginRequiredMixin, SingleTableView):
    model = models.Empleado
    table_class = empleadoTables.EmpleadoTable
    template_name = 'comunes/tabla2_without_filter.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['appdomain'] = "empresa" or __package__.split('.')[1] 
        return context
        
    def get_queryset(self):
        return models.Empleado.objects.filter(active=True)


class EmpleadoCreateView(PermissionRequiredMixin, generic.CreateView):
    permission_required = 'empleado.add_empleado'

    model = models.Empleado
    form_class = empleadoForms.EmpleadoForm
    template_name = 'comunes/formulario.html'
    form_title = 'Nueva Empleado'

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


class EmpleadoDetailView(PermissionRequiredMixin, generic.DetailView):
    permission_required = 'empleado.view_empleado'
    model = models.Empleado
    template_name = 'empleado/detalle.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # comprobamos la existencia de la variable de sesion 'tab'
        if 'tab' in self.request.session.keys():
            context['tab'] = self.request.session['tab']
        else:
            context['tab'] = 'datos'
        # context['domicilio'] = Domicilio.objects.filter(
        #     empleado_id=context['empleado'].persona_id
        # )
        # context['comunicaciones'] = Comunicacion.objects.filter(
        #     empleado_id=context['empleado'].persona_id
        # ).order_by('tipo')
        # context['denuncias'] = models.Denuncia_ART.objects.filter(empleado_id=context['empleado'].persona_id)
        # context['activos'] = models.ActivoMantenimientoView.objects.filter(responsable_id=context['empleado'].persona_id)
        return context


class EmpleadoUpdateView(PermissionRequiredMixin, generic.UpdateView):
    permission_required = ['empleado.add_empleado', 'empleado.change_empleado']
    model = models.Empleado
    form_class = empleadoForms.EmpleadoForm
    template_name = 'comunes/formulario.html'
    form_title = 'Modificación de Empleado'

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


class EmpleadoDeleteView(PermissionRequiredMixin, generic.DeleteView):
    permission_required = 'empleado.delete_empleado'
    model = models.Empleado
    success_message = "Registro eliminado correctamente"

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):    
        redirect = self.request.GET.get('next')
        if redirect:
            return redirect
        return reverse_lazy('empleado:list')


def EmpleadoDetailAjax(request):
    empleadoId = request.GET['pk']
    solapa = request.GET['tab']
    request.session['tab'] = solapa

    if solapa == 'datos':
        template = 'empleado/solapas/_info.html'
        info = models.Empleado.objects.get(persona_id=empleadoId)
        context = {'object': info}
        return render(request, template, context)

    elif solapa == 'denuncias':
        data = models.Denuncia_ART.objects.filter(empleado_id=empleadoId).filter(active=True)
        template = 'empleado/solapas/_denuncias.html'

    elif solapa == 'activos':
        data = models.Activo.objects.filter(responsable_id=empleadoId).filter(active=True)
        template = 'empleado/solapas/_activos.html'

    elif solapa == 'vacaciones':
        data = models.Vacaciones.objects.filter(empleado_id=empleadoId).filter(active=True)
        template = 'empleado/solapas/_vacaciones.html'

    return render(request, template, {'object_list': data, 'info_panel': 'panel'})


def EmpleadoDetailPanelAjax(request):
    empleadoId = request.GET['pk']

    if request.session['tab'] != 'vacaciones':
        data = []  # models.Comunicacion.objects.filter(empleado_id=empleadoId).order_by('tipo')
        context = {'object_list': data }
        template = 'empleado/solapas/_info_panel.html'
    else:
        data = models.Empleado.objects.get(persona_id=empleadoId)
        context = {'empleado': data}
        template = 'empleado/solapas/_vacaciones_panel.html'

    return render(request, template, context)