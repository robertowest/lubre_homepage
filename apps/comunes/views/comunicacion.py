from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from apps.comunes.models import Comunicacion as ComunicacionModel
from apps.comunes.forms.comunicacion import ComunicacionForm, ComunicacionFilterFormHelper
from apps.comunes.filters import ComunicacionListFilter
from apps.comunes.tables import ComunicacionTable
from apps.comunes.utils import PagedFilteredTableView


class ComunicacionTemplateView(TemplateView):
    # si no existe página index llamamos a otra función
    def get(self, request, *args, **kwargs):
        return ComunicacionListView.as_view()(request)


class ComunicacionListView(PagedFilteredTableView):
    model = ComunicacionModel
    template_name = 'comunes/tabla2.html'

    table_class = ComunicacionTable
    filter_class = ComunicacionListFilter
    formhelper_class = ComunicacionFilterFormHelper

    # def get_queryset(self):
    #     return ComunicacionModel.objects.filter(active=True)[:50]
 
 
class ComunicacionCreateView(CreateView):
    model = ComunicacionModel
    form_class = ComunicacionForm
    template_name = 'comunes/formulario.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        return response
 
 
class ComunicacionDetailView(DetailView):
    model = ComunicacionModel
    template_name = 'comunes/detalle.html'
 
 
class ComunicacionUpdateView(UpdateView):
    model = ComunicacionModel
    form_class = ComunicacionForm
    template_name = 'comunes/formulario.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        # terminamos, ¿hacia dónde vamos?
        if 'previous_url' in self.request._post:
            return HttpResponseRedirect(self.request._post['previous_url'])
        return response

 
class ComunicacionDeleteView(DeleteView):
    model = ComunicacionModel
    success_message = "Registro eliminado correctamente"

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        redirect = self.request.GET.get('next')
        if redirect:
            return redirect
        return reverse_lazy('comunicacion:list')
