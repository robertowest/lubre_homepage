from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from django_tables2 import SingleTableView

from apps.rrhh import models
from apps.rrhh.forms import activoForms as forms
from apps.rrhh.tables import activoTables as tables


class ActivoTemplateView(generic.TemplateView):
    # si no existe página index llamamos a otra función
    def get(self, request, *args, **kwargs):
        return ActivosListView.as_view()(request)


class ActivosListView(LoginRequiredMixin, SingleTableView):
    model = models.Activo
    table_class = tables.ActivoTable
    template_name = 'comunes/tabla2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['appdomain'] = "empresa" or __package__.split('.')[1] 
        return context
        
    def get_queryset(self):
        return models.Activo.objects.filter(active=True)


class ActivoCreateView(PermissionRequiredMixin, generic.CreateView):
    permission_required = 'activo.add_activo'

    model = models.Activo
    form_class = forms.ActivoForm
    template_name = 'comunes/formulario.html'
    form_title = 'Nueva Activo'

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


class ActivoDetailView(PermissionRequiredMixin, generic.DetailView):
    permission_required = 'activo.view_activo'
    model = models.Activo
    template_name = 'activo/detalle.html'


class ActivoUpdateView(PermissionRequiredMixin, generic.UpdateView):
    permission_required = ['activo.add_activo', 'activo.change_activo']
    model = models.Activo
    form_class = forms.ActivoForm
    template_name = 'comunes/formulario.html'
    form_title = 'Modificación de Activo'

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


class ActivoDeleteView(PermissionRequiredMixin, generic.DeleteView):
    permission_required = 'activo.delete_activo'
    model = models.Activo
    success_message = "Registro eliminado correctamente"

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):    
        redirect = self.request.GET.get('next')
        if redirect:
            return redirect
        return reverse_lazy('activo:list')
