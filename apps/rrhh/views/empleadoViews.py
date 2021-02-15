from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from django_filters.views import FilterView
from django_tables2 import SingleTableView

from apps.comunes.models import Comunicacion
from apps.rrhh import models
from apps.rrhh.filters import empleadoFilters as filters
from apps.rrhh.forms import empleadoForms as forms
from apps.rrhh.tables import empleadoTables as tables
from apps.rrhh.tables import denunciaTables, activoTables

from apps.comunes.utils import PagedFilteredTableView


class EmpleadoTemplateView(generic.TemplateView):
    # si no existe página index llamamos a otra función
    def get(self, request, *args, **kwargs):
        return EmpleadosListView.as_view()(request)


class EmpleadosListView(LoginRequiredMixin, PagedFilteredTableView):
    model = models.Vacaciones
    table_class = tables.EmpleadoTable
    filter_class = filters.EmpleadoFilter
    formhelper_class = filters.EmpleadoFilterForm
    template_name = 'comunes/tabla2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['appdomain'] = "empresa" or __package__.split('.')[1] 
        return context
        
    def get_queryset(self):
        return models.Empleado.objects.filter(active=True)


class EmpleadoCreateView(PermissionRequiredMixin, generic.CreateView):
    permission_required = 'empleado.add_empleado'

    model = models.Empleado
    form_class = forms.EmpleadoForm
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
        return context


class EmpleadoUpdateView(PermissionRequiredMixin, generic.UpdateView):
    permission_required = ['empleado.add_empleado', 'empleado.change_empleado']
    model = models.Empleado
    form_class = forms.EmpleadoForm
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



# -----------------------------------------------------------------------------
# solapas
# -----------------------------------------------------------------------------
class TabDatosDetailView(PermissionRequiredMixin, generic.DetailView):
    permission_required = 'empleado.view_empleado'
    model = models.Empleado
    template_name = 'empleado/solapas/datos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.request.session['tab'] = self.request.GET['tab']
        return context        


class TabDenunciasListView(LoginRequiredMixin, SingleTableView):
    model = models.Denuncia_ART
    table_class = denunciaTables.DenunciaTable
    template_name = 'empleado/solapas/denuncias.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.request.session['tab'] = self.request.GET['tab']
        return context        

    def get_queryset(self):
        return models.Denuncia_ART.objects.filter(empleado=self.kwargs['pk']).filter(active=True)


class TabActivosListView(LoginRequiredMixin, SingleTableView):
    model = models.Activo
    table_class = activoTables.ActivoTable
    template_name = 'empleado/solapas/activos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.request.session['tab'] = self.request.GET['tab']
        return context
        
    def get_queryset(self):
        return models.Activo.objects.filter(responsable=self.kwargs['pk']).filter(active=True)


class TabVacacionesListView(LoginRequiredMixin, SingleTableView):
    pass