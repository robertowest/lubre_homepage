import datetime

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from django_filters.views import FilterView
from django_tables2 import SingleTableView

from apps.rrhh import models
from apps.rrhh.filters import vacacionesFilters as filters
from apps.rrhh.forms import vacacionesForms as forms
from apps.rrhh.tables import vacacionesTables as tables

from apps.comunes.utils import PagedFilteredTableView


class VacacionesTemplateView(generic.TemplateView):
    # si no existe página index llamamos a otra función
    def get(self, request, *args, **kwargs):
        return VacacionesListView.as_view()(request)


class VacacionesListView(LoginRequiredMixin, PagedFilteredTableView):
    model = models.Vacaciones
    table_class = tables.VacacionesTable
    filter_class = filters.VacacionesFilter
    formhelper_class = filters.VacacionesFilterForm
    template_name = 'comunes/tabla2.html'

    # def get_queryset(self):
    #     if 'periodo' in self.kwargs:
    #         anio = self.kwargs['periodo']
    #     else:
    #         anio = datetime.datetime.now().year
    #     return self.model.objects.filter(active=True).filter(periodo=anio)


class VacacionesCreateView(PermissionRequiredMixin, generic.CreateView):
    permission_required = 'vacaciones.add_vacaciones'

    model = models.Vacaciones
    form_class = forms.VacacionesForm
    template_name = 'comunes/formulario.html'
    form_title = 'Nueva Vacaciones'

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


class VacacionesDetailView(PermissionRequiredMixin, generic.DetailView):
    permission_required = 'vacaciones.view_vacaciones'
    model = models.Vacaciones
    template_name = 'comunes/detalle.html'


class VacacionesUpdateView(PermissionRequiredMixin, generic.UpdateView):
    permission_required = ['vacaciones.add_vacaciones', 'vacaciones.change_vacaciones']
    model = models.Vacaciones
    form_class = forms.VacacionesForm
    template_name = 'comunes/formulario.html'
    form_title = 'Modificación de Vacaciones'

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


class VacacionesDeleteView(PermissionRequiredMixin, generic.DeleteView):
    permission_required = 'vacaciones.delete_vacaciones'
    model = models.Vacaciones
    success_message = "Registro eliminado correctamente"

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):    
        redirect = self.request.GET.get('next')
        if redirect:
            return redirect
        return reverse_lazy('vacaciones:list')
