from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from django_tables2 import SingleTableView

from apps.rrhh import models
from apps.rrhh.forms import denunciaForms as forms
from apps.rrhh.tables import denunciaTables as tables


class DenunciaTemplateView(generic.TemplateView):
    # si no existe página index llamamos a otra función
    def get(self, request, *args, **kwargs):
        return DenunciasListView.as_view()(request)


class DenunciasListView(LoginRequiredMixin, SingleTableView):
    model = models.Denuncia_ART
    table_class = tables.DenunciaTable
    template_name = 'comunes/tabla2_without_filter.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['appdomain'] = "denuncia" or __package__.split('.')[1] 
        return context
        
    def get_queryset(self):
        return models.Denuncia_ART.objects.filter(active=True)


class DenunciaCreateView(PermissionRequiredMixin, generic.CreateView):
    permission_required = 'denuncia_art.add_denuncia'

    model = models.Denuncia_ART
    form_class = forms.DenunciaForm
    template_name = 'comunes/formulario.html'
    form_title = 'Nueva Denuncia'

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


class DenunciaDetailView(PermissionRequiredMixin, generic.DetailView):
    permission_required = 'denuncia_art.view_denuncia'
    model = models.Denuncia_ART
    template_name = 'comunes/detalle.html'


class DenunciaUpdateView(PermissionRequiredMixin, generic.UpdateView):
    permission_required = ['denuncia.add_denuncia', 'denuncia.change_denuncia']
    model = models.Denuncia_ART
    form_class = forms.DenunciaForm
    template_name = 'comunes/formulario.html'
    form_title = 'Modificación de Denuncia'

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


class DenunciaDeleteView(PermissionRequiredMixin, generic.DeleteView):
    permission_required = 'denuncia_art.delete_denuncia'
    model = models.Denuncia_ART
    success_message = "Registro eliminado correctamente"

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):    
        redirect = self.request.GET.get('next')
        if redirect:
            return redirect
        return reverse_lazy('denuncia:list')
