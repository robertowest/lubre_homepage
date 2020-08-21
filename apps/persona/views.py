from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic

from . import forms, models
from apps.comunes.models import Comunicacion as ComunicacionModel
from apps.comunes.models import Domicilio as DomicilioModel
from apps.comunes.forms.comunicacion import ComunicacionForm
from apps.comunes.forms.domicilio import DomicilioForm


# Create your views here.
def home(request):
    # return render(request, 'base.html', context={},)
    return render(request, 'ejemplos/register.html', context={},)


class PersonaTemplateView(generic.TemplateView):
    # si no existe página index llamamos a otra función
    def get(self, request, *args, **kwargs):
        return PersonasListView.as_view()(request)


class PersonasListView(generic.ListView):
    model = models.Persona
    template_name = 'persona/tabla_filtro.html'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['app_name'] = __package__.split('.')[1]
    #     context['model_name'] = models.Persona._meta.verbose_name_plural.title()
    #     context['object_list'] = models.Persona.objects.filter(active=True)
    #     return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_name'] = __package__.split('.')[1]
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get('search1') 
        if search:
            return qs.filter(nombre__icontains=search).filter(active=True)
        else: 
            return qs.filter(id=0)


class PersonaCreateView(generic.CreateView):  # LoginRequiredMixin
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


class PersonaDetailView(generic.DetailView):
    model = models.Persona
    # template_name = 'comunes/detalle.html'
    template_name = '{app}/detalle.html'.format(app=model._meta.verbose_name.lower())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comunicaciones'] = context['persona'].comunicaciones.filter(active=True)
        return context


class PersonaUpdateView(generic.UpdateView):
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


class PersonaDeleteView(generic.DeleteView):
    pass


class CreateContactView(generic.CreateView):
    model = ComunicacionModel
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


class CreateAddressView(generic.CreateView):
    model = DomicilioModel
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
        persona.domicilios.add(self.object)

        # terminamos, ¿hacia dónde vamos?
        if 'previous_url' in self.request._post:
            return HttpResponseRedirect(self.request._post['previous_url'])
        return response


@login_required(login_url='/accounts/login/')
def persona_contacto_eliminar(request, pk, fk):
    p = models.Persona.objects.get(id=pk)
    p.comunicaciones.remove(fk)
    url = reverse('persona:detail', args=(), kwargs={'pk': pk})
    return HttpResponseRedirect(url)
