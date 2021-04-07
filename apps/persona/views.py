from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, QueryDict
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic

from django_filters.views import FilterView
from django_tables2 import RequestConfig
from django_tables2.views import SingleTableMixin
from django_tables2.paginators import LazyPaginator

from . import filters, forms, models, tables
from apps.empresa.models import Comercial

from apps.comunes.models import Comunicacion as ComunicacionModel
from apps.comunes.models import Domicilio as DomicilioModel
from apps.comunes.forms.comunicacion import ComunicacionForm
from apps.comunes.forms.domicilio import DomicilioForm
from apps.comunes.utils import PagedFilteredTableView

# asociar persona con comunicación
from apps.comunes.models import Comunicacion
from apps.comunes.filters import ComunicacionFindFilter
from apps.comunes.tables import ComunicacionFindTable
from apps.comunes.forms.comunicacion import ComunicacionFilterFormModal


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
        # busqueda modal
        objetos_ajax_asociar_comunicacion(self.request, context)
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


class CreateContactView(PermissionRequiredMixin, generic.CreateView):
    permission_required = 'comunes.add_comunicacion'

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


class CreateAddressView(PermissionRequiredMixin, generic.CreateView):
    permission_required = 'comunes.add_domicilio'

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
        persona.domicilio = self.object
        persona.save()

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


def objetos_ajax_asociar_comunicacion(request, context):
    if request.GET:
        filter = ComunicacionFindFilter(request.GET, queryset=Comunicacion.objects.all())
    else:
        from django.http import QueryDict
        qd = QueryDict('tipo=3&texto=¿Qué busca?&active=True&submit=Filtrar')
        filter = ComunicacionFindFilter(qd, queryset=Comunicacion.objects.all())

    filter.form.helper = ComunicacionFilterFormModal()
    table = ComunicacionFindTable(filter.qs[:10])   # solo 10 registros
    RequestConfig(request).configure(table)
    context['filter'] = filter
    context['table'] = table
    return context


def ajax_abrir_comunicacion(request):
    # from django.template import Context, Template
    # t = Template("{% render_table table %}")
    # c = Context({'filter': filter})
    # return t.render(c)

    # context = {
    #             'filter': ComunicacionFindFilter(request.GET, queryset=Comunicacion.objects.all()),
    #             'table': ComunicacionFindTable(filter.qs[:10])
    #           }
    # return render(request, 'prueba/includes/find_table_modal.html', context)

    filter = ComunicacionFindFilter(request.GET, queryset=Comunicacion.objects.all())
    filter.form.helper = ComunicacionFilterFormModal()
    table = ComunicacionFindTable(filter.qs[:10])   # solo 10 registros
    RequestConfig(request).configure(table)
    context = {'filter': filter, 'table': table }
    return render(request, 'includes/_modal_find_data.html', context)


def ajax_asociar_comunicacion(request, persona_id, comunicacion_id):
    persona = models.Persona.objects.get(id=persona_id)
    comunica = Comunicacion.objects.get(id=comunicacion_id)
    persona.comunicaciones.add(comunica)
    persona.save()
    # template_name = 'comunes/detalle.html'
    template_name = '{app}/detalle.html'.format(app=model._meta.verbose_name.lower())
    return render(request, template_name, context={'object':persona})
