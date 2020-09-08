import os

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_list_or_404, get_object_or_404
from django.urls import resolve, reverse, reverse_lazy
from django.views import generic
from django_tables2 import SingleTableView

from . import filters, forms, models, tables

from apps.comunes.models import Comunicacion as ComunicacionModel
from apps.comunes.models import Domicilio as DomicilioModel
from apps.comunes.forms.comunicacion import ComunicacionForm
from apps.comunes.forms.domicilio import DomicilioForm
from apps.comunes.utils import PagedFilteredTableView

from apps.persona.models import Persona as ContactoModel
from apps.persona.forms import PersonaForm as ContactoForm


# -----------------------------------------------------------------------------
# Empresa
# -----------------------------------------------------------------------------


class EmpresaTemplateView(LoginRequiredMixin, generic.TemplateView):
    # app=__package__.split('.')[1]     --> lo obtiene de urls.py
    # model._meta.verbose_name.lower()  --> lo obtiene de models.py
    model = models.Empresa
    template_name = '{app}/index.html'.format(app=__package__.split('.')[1])

    def get_context_data(self, **kwargs):
        model = self.model
        context = super().get_context_data(**kwargs)
        context['actividades'] = model.objects.values('actividad', 'actividad__nombre').annotate(contador=Count('id'))
        context['comerciales'] = model.objects.values('comercial', 'comercial__persona__apellido').annotate(contador=Count('id'))
        return context


class EmpresaListView(LoginRequiredMixin, PagedFilteredTableView):
    model = models.Empresa
    filter_class = filters.EmpresaFilter
    table_class = tables.EmpresaTable
    formhelper_class = forms.EmpresaFilterForm
    template_name = 'comunes/tabla2.html'

    def get_queryset(self):
        return models.Empresa.objects.filter(active=True)


class EmpresaCreateView(LoginRequiredMixin, generic.CreateView):    # LoginRequiredMixin
    model = models.Empresa
    form_class = forms.EmpresaForm
    template_name = 'comunes/formulario.html'
    form_title = 'Nueva Empresa'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = self.form_title
        return context

    # def get_success_url(self):
    #     name = self.model._meta.verbose_name.lower()
    #     return reverse_lazy('{app}:detail'.format(app=name), args=(self.object.pk,))

    def form_valid(self, form):
        response = super().form_valid(form)
        # terminamos, ¿hacia dónde vamos?
        if 'previous_url' in self.request._post:
            return HttpResponseRedirect(self.request._post['previous_url'])
        return response


class EmpresaDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Empresa
    template_name = 'empresa/detalle.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comunicaciones'] = context['empresa'].comunicaciones.filter(active=True)
        context['actividades'] = context['empresa'].actividades.filter(active=True)
        return context


class EmpresaUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = models.Empresa
    form_class = forms.EmpresaForm
    template_name = 'comunes/formulario.html'
    form_title = 'Modificación de Empresa'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = self.form_title
        return context

    # def get_success_url(self):
    #     name = self.model._meta.verbose_name.lower()
    #     # return reverse_lazy('{app}:detail'.format(app=name), args=(self.kwargs['pk'],))
    #     return reverse_lazy('{app}:detail'.format(app=name), args=(self.object.pk,))

    def form_valid(self, form):
        response = super().form_valid(form)
        # terminamos, ¿hacia dónde vamos?
        if 'previous_url' in self.request._post:
            return HttpResponseRedirect(self.request._post['previous_url'])
        return response


class EmpresaDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = models.Empresa
    success_message = "Registro eliminado correctamente"

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        redirect = self.request.GET.get('next')
        if redirect:
            return redirect
        #reverse_lazy('empresa:detail', args=(self.object.pk,))
        return reverse_lazy('empresa:list')


def empresa_actividad(request, empId, actId):
    ea = models.EmpresaActividades.objects.filter(empresa=empId).filter(actividad=actId)
    # http://localhost:8000/empresa/6027/actividad/7/
    # return EmpActDetailView.as_view()(request, pk=ea[0].id)
    # http://localhost:8000/empresa_actividad/2859/
    url = reverse('empresa_actividad:detail', args=(), kwargs={'pk': ea[0].id})
    return HttpResponseRedirect(url)


# -----------------------------------------------------------------------------
# Empresas filtradas por Actividades y Comerciales
# -----------------------------------------------------------------------------


class FilterListView_old(LoginRequiredMixin, generic.ListView):
    model = models.Empresa
    # template_name = '{app}/list.html'.format(app=model._meta.verbose_name.lower())
    # comprobamos si existe un template personalizado, sino utilizamos el comun
    template = '{path}/{app}/templates/{app}/tabla.html'.format(
        path=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        app=model._meta.app_label,
    )
    if os.path.exists(template):
        template_name = '{app}/tabla.html'.format(app=model._meta.app_label)
    else:
        template_name = 'comunes/tabla.html'

    def url_name(self):
        attrib = resolve(self.request.path)
        return getattr(attrib, 'url_name', 'all')

    def get_queryset(self):
        # attrib = resolve(self.request.path)
        # name = getattr(attrib, 'url_name', 'all')
        name = self.url_name()
        if self.kwargs['filtro'] == 0:
            self.kwargs['filtro'] = None
        if name == 'filtro_actividad':
            return self.model.objects \
                   .filter(actividad=self.kwargs['filtro']) \
                   .filter(active=True) \
                   .order_by('razon_social')
        if name == 'filtro_comercial':
                   # .filter(modified__isnull=True) \
            return self.model.objects \
                   .filter(comercial=self.kwargs['filtro']) \
                   .filter(active=True) \
                   .order_by('razon_social')
        return self.model.objects.all().order_by('razon_social')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.url_name()
        if name == 'filtro_actividad':
            context['filtro'] = 'filtrado por Actividad'
        if name == 'filtro_comercial':
            context['filtro'] = 'filtrado por Comercial'
        return context

class FilterListView(LoginRequiredMixin, PagedFilteredTableView):
    model = models.Empresa
    filter_class = filters.EmpresaFilter
    table_class = tables.EmpresaTable
    formhelper_class = forms.EmpresaFilterForm  # params={'tipo': 'filtrado'}
    template_name = 'comunes/tabla2.html'

    def url_name(self):
        attrib = resolve(self.request.path)
        return getattr(attrib, 'url_name', 'all')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.url_name()
        if name == 'filtro_actividad':
            context['filtro'] = 'filtrado por Actividad'
        if name == 'filtro_comercial':
            context['filtro'] = 'filtrado por Comercial'
        return context

    def get_queryset(self):
        if ('actividad' in self.request.GET and self.request.GET['actividad'] != ''):
            data = self.model.objects \
                   .filter(actividad=self.request.GET['actividad']) \
                   .order_by('razon_social')
        elif ('comercial' in self.request.GET and self.request.GET['comercial'] != ''):
            # .filter(modified__isnull=True) \
            data = self.model.objects \
                   .filter(comercial=self.request.GET['comercial']) \
                   .order_by('razon_social')
        else:
            return self.model.objects.all().order_by('razon_social')

        # if ('active' in self.request.GET):
        #     return data.filter(active=self.request.GET['active'])
        return data

# -----------------------------------------------------------------------------
# Tablas relacionadas a la empresa
# -----------------------------------------------------------------------------


class CreateComunicationView(LoginRequiredMixin, generic.CreateView):
    model = ComunicacionModel
    form_class = ComunicacionForm
    template_name = 'comunes/formulario.html'
    form_title = 'Nuevo Tipo de Comunicación'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = self.form_title
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        
        # grabamos el objeto para obtener identificador
        self.object = form.save()
        # obtenemos el objeto primario
        empresa = models.Empresa.objects.get(id=self.kwargs['fk'])
        # creamos la asociación
        empresa.comunicaciones.add(self.object)
        
        # terminamos, ¿hacia dónde vamos?
        if 'previous_url' in self.request._post:
            return HttpResponseRedirect(self.request._post['previous_url'])
        return response


@login_required(login_url='/accounts/login/')
def comunication_delete(request, empID, conID):
    obj = models.EmpresaComunicaciones.objects.filter(empresa_id=empID, comunicacion_id=conID)
    obj.delete()
    url = reverse('empresa:detail', args=(), kwargs={'pk': empID})
    return HttpResponseRedirect(url)


class CreateActividadView(LoginRequiredMixin, generic.CreateView):
    # model = models.Actividad
    # form_class = forms.ActividadForm
    # template_name = 'comunes/formulario.html'
    # form_title = 'Nueva Subactividad'

    # def get_context_data(self, **kwargs):
    #     context = super(CreateActividadView, self).get_context_data(**kwargs)        
    #     context['form_title'] = self.form_title
    #     return context

    # def form_valid(self, form):
    #     response = super().form_valid(form)

    #     # grabamos el objeto para obtener identificador
    #     self.object = form.save()
    #     # obtenemos el objeto primario
    #     empresa = models.Empresa.objects.get(id=self.kwargs['fk'])
    #     # creamos la asociación
    #     empresa.actividades.add(self.object)

    #     # terminamos, ¿hacia dónde vamos?
    #     if 'previous_url' in self.request._post:
    #         return HttpResponseRedirect(self.request._post['previous_url'])
    #     return response
    pass


class ActividadMultiListView(LoginRequiredMixin, generic.ListView):
    # , generic.edit.ModelFormMixin
    model = models.Actividad
    form_title = 'Asociar Subactividad'
    template_name = 'actividad/tabla.html'

    def get_queryset(self):
        ordering = 'CASE WHEN parent_id IS Null THEN id ELSE parent_id END * 1000 + id'
        qs = models.Actividad.objects.filter(active=True).extra(select={'criterio': ordering}, order_by=('criterio',))
        return qs

    def post(self, request, *args, **kwargs):
        # listado de id seleccionados
        id_list = request.POST.getlist('checkboxname')

        # recuperamos el registro de la empresa
        empresa = models.Empresa.objects.get(id=kwargs['fk'])
        for actividad_id in id_list:
            actividad = models.Actividad.objects.get(id=actividad_id)
            empresa.actividades.add(actividad)
        empresa.save()

        # return HttpResponseRedirect('/jobs/')
        # context = {}  #  set your context
        # return super(TemplateView, self).render_to_response(context)
        # return HttpResponse('Datos grabados correctamente.')

        # return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

        if 'previous_url' in self.request._post:
            return HttpResponseRedirect(self.request._post['previous_url'])
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



# -----------------------------------------------------------------------------
# Actividad
# -----------------------------------------------------------------------------


class ActividadTemplateView(LoginRequiredMixin, generic.TemplateView):
    def get(self, request, *args, **kwargs):
        return ActividadListView.as_view()(request)


class ActividadListView(LoginRequiredMixin, SingleTableView):  # PagedFilteredTableView
    model = models.Actividad
    # filter_class = filters.ActividadFilter  # (initial={'active': True})
    table_class = tables.ActividadTable
    # formhelper_class = forms.ActividadFilterForm    # (initial = {'active': True})
    template_name = 'comunes/tabla2_not_filter.html'

    def get_queryset(self):
        ordering = 'IFNULL(parent_id, id)'
        qs = models.Actividad.objects.all().filter(active=True).extra(select={'grupo': ordering}, order_by=('grupo','parent_id','nombre'))
        return qs


class ActividadCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.Actividad
    form_class = forms.ActividadForm
    template_name = 'comunes/formulario.html'
    form_title = 'Nueva Actividad'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = self.form_title
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        # terminamos, ¿hacia dónde vamos?
        if 'previous_url' in self.request._post:
            return HttpResponseRedirect(self.request._post['previous_url'])
        return response


class ActividadDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Actividad
    template_name = 'comunes/detalle.html'


class ActividadUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = models.Actividad
    form_class = forms.ActividadForm
    template_name = 'comunes/formulario.html'
    form_title = 'Modificación de Actividad'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = self.form_title
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        # terminamos, ¿hacia dónde vamos?
        if 'previous_url' in self.request._post:
            return HttpResponseRedirect(self.request._post['previous_url'])
        return response


class ActividadDeleteView(LoginRequiredMixin, generic.DeleteView):
    pass


# -----------------------------------------------------------------------------
# Empresa Actividad
# -----------------------------------------------------------------------------


class EmpActDetailView(LoginRequiredMixin, generic.DetailView):
    # EmpresaActividades.objects.filter(empresa=6027).filter(actividad=7)
    model = models.EmpresaActividades
    template_name = 'empresa_actividad/detalle.html'

    # def get_object(self):
    #     ea = models.EmpresaActividades.objects.filter(empresa=6027).filter(actividad=7)
    #     return get_object_or_404(models.EmpresaActividades, pk=ea[0].id)

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        context['contactos'] = models.EmpresaActividadContactos.objects.filter(empresa_actividad_id=pk)
        context['domicilios'] = models.EmpresaActividadDomicilios.objects.filter(empresa_actividad_id=pk)
        # context['contactos'] = context['empresaactividades'].ea_contactos.instance
        # context['domicilios'] = context['empresaactividades'].ea_domicilios.instance
        return context


class CreateAddressView(LoginRequiredMixin, generic.CreateView):
    model = DomicilioModel
    form_class = DomicilioForm
    template_name = 'comunes/formulario.html'
    form_title = 'Nuevo Domicilio'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = self.form_title
        return context

    def form_valid(self, form):
        response = super().form_valid(form)

        # grabamos el objeto para obtener identificador
        self.object = form.save()
        # obtenemos el objeto primario 
        ea = models.EmpresaActividades.objects.get(id=self.kwargs['pk'])
        # creamos la asociación con empresa-actividad
        # ea.ea_domicilios.add(self.object)
        models.EmpresaActividadDomicilios(
            empresa_actividad = ea, 
            domicilio = self.object
        ).save()

        # terminamos, ¿hacia dónde vamos?
        if 'previous_url' in self.request._post:
            return HttpResponseRedirect(self.request._post['previous_url'])
        return response


class CreateContactView(LoginRequiredMixin, generic.CreateView):
    model = ContactoModel
    form_class = ContactoForm
    template_name = 'comunes/formulario.html'
    form_title = 'Nuevo Contacto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = self.form_title
        return context

    def form_valid(self, form):
        response = super().form_valid(form)

        # grabamos el objeto para obtener identificador
        self.object = form.save()
        # obtenemos el objeto primario
        ea = models.EmpresaActividades.objects.get(id=self.kwargs['pk'])
        # creamos la asociación con empresa-actividad
        # ea.contactos.add(self.object)
        models.EmpresaActividadContactos(
            empresa_actividad = ea,
            persona = self.object
        ).save()

        # terminamos, ¿hacia dónde vamos?
        if 'previous_url' in self.request._post:
            return HttpResponseRedirect(self.request._post['previous_url'])
        return response


@login_required(login_url='/accounts/login/')
def buscar_contacto(request, pk):
    # SELECT * FROM `persona` WHERE id NOT IN (SELECT persona_id FROM comercial) 
    # obj_list = ContactoModel.objects.filter(active=True).order_by('apellido', 'nombre')
    # eliminamos las personas que son comerciales de la empresa
    inner_qs = models.Comercial.objects.all()
    obj_list = ContactoModel.objects.exclude(id__in=inner_qs) \
                    .filter(active=True).order_by('apellido', 'nombre')
    context = {
        'tableID': 'dataTableModal',
        'object_list': obj_list,
        'empresa_actividad_id': pk,
    }
    return render(request, 'empresa_actividad/includes/_modal_contacto.html', context)


@login_required(login_url='/accounts/login/')
def asociar_contacto(request, relaId, conId):
    # empresa_actividad_id = relaId
    # contacto_id = conId
    relacion = models.EmpresaActividadContactos()
    relacion.empresa_actividad_id = relaId
    relacion.persona_id = conId
    relacion.save()
    url = reverse('empresa_actividad:detail', args=(), kwargs={'pk': relaId})
    return HttpResponseRedirect(url)


# -----------------------------------------------------------------------------
# Empresa Actividad Contacto
# -----------------------------------------------------------------------------

@login_required(login_url='/accounts/login/')
def eac_delete(request, eacId):
    obj = models.EmpresaActividadContactos.objects.get(pk=eacId)
    pk = obj.empresa_actividad_id
    obj.delete()
    url = reverse('empresa_actividad:detail', args=(), kwargs={'pk': pk})
    return HttpResponseRedirect(url)

@login_required(login_url='/accounts/login/')
def eac_asignar_cargo(request, eaId, eacId):
    if request.method == "GET":
        context = {
            'object': models.EmpresaActividadContactos.objects.get(id=eacId),
            'empresa_actividad_id': eaId,
            'empresa_actividad_contacto_id': eacId,
        }
        return render(request, 'empresa_actividad/includes/_modal_asignar_cargo.html', context)
    elif request.method == "POST":
        relacion = models.EmpresaActividadContactos.objects.get(id=eacId)
        relacion.cargo = request.POST['cargo']
        relacion.save()
    return HttpResponseRedirect(reverse('empresa_actividad:detail', args=(), kwargs={'pk': eaId}))


# -----------------------------------------------------------------------------
# Empresa Actividad Domicilio
# -----------------------------------------------------------------------------

@login_required(login_url='/accounts/login/')
def reasignar_domicilio(request, eaId, eadId):
    empresa = models.EmpresaActividades.objects.get(id=eaId).empresa_id
    obj_list = models.EmpresaActividades.objects.filter(empresa_id=empresa)
    context = {
        'object_list': obj_list,
        'empresa_actividad_id': eaId,
        'empresa_actividad_domicilio_id': eadId,
    }
    return render(request, 'empresa_actividad/includes/_modal_reasigna.html', context)

@login_required(login_url='/accounts/login/')
def reasignar_domicilio_ex(request, eaId, eadId):
    relacion = models.EmpresaActividadDomicilios.objects.get(id=eadId)
    relacion.empresa_actividad_id = eaId
    relacion.save()
    url = reverse('empresa_actividad:detail', args=(), kwargs={'pk': eaId})
    return HttpResponseRedirect(url)

@login_required(login_url='/accounts/login/')
def ead_delete(request, eadId):
    obj = models.EmpresaActividadDomicilios.objects.get(pk=eadId)
    pk = obj.empresa_actividad_id
    obj.delete()
    url = reverse('empresa_actividad:detail', args=(), kwargs={'pk': pk})
    return HttpResponseRedirect(url)


# -----------------------------------------------------------------------------
# Comercial
# -----------------------------------------------------------------------------


class ComercialTemplateView(LoginRequiredMixin, generic.TemplateView):
    def get(self, request, *args, **kwargs):
        return ComercialListView.as_view()(request)


class ComercialListView(LoginRequiredMixin, PagedFilteredTableView):
    model = models.Comercial
    filter_class = filters.ComercialFilter  # (initial={'active': True})
    table_class = tables.ComercialTable
    formhelper_class = forms.ComercialFilterForm    # (initial = {'active': True})
    template_name = 'comunes/tabla2.html'

    # def get_queryset(self):
    #     return models.Comercial.objects.filter(active=True)


class ComercialCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.Comercial
    form_class = forms.ComercialForm
    template_name = 'comunes/formulario.html'
    form_title = 'Nuevo Comercial'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = self.form_title
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        # terminamos, ¿hacia dónde vamos?
        if 'previous_url' in self.request._post:
            return HttpResponseRedirect(self.request._post['previous_url'])
        return response


class ComercialDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Comercial
    template_name = 'comunes/detalle.html'


class ComercialUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = models.Comercial
    form_class = forms.ComercialForm
    template_name = 'comunes/formulario.html'
    form_title = 'Modificación del Comercial'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = self.form_title
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        # terminamos, ¿hacia dónde vamos?
        if 'previous_url' in self.request._post:
            return HttpResponseRedirect(self.request._post['previous_url'])
        return response


class ComercialDeleteView(LoginRequiredMixin, generic.DeleteView):
    pass


# ----------------------------------------------------------------------------------
# quitar despues de haber controlado todos los clientes por parte de los comerciales
# ----------------------------------------------------------------------------------
from next_prev import next_in_order, prev_in_order

@login_required(login_url='/accounts/login/')
def Recorrer(request):
    comercial = models.Comercial.objects.get(usuario=request.user)
    empresa = models.Empresa.objects.filter(comercial=comercial).order_by('razon_social').first()
    url = "/empresa/recorrer/" + str(empresa.id) + "/"
    # return render(request, 'accounts/profile.html', {'object': empresa})
    # return HttpResponse(url)
    return HttpResponseRedirect(url)


class EmpresaBrowseView(generic.DetailView):
    model = models.Empresa
    form_class = forms.EmpresaForm
    # model = models.Empresa.objects.filter(comercial=context['comercial']).get(id=context['empresa'])
    template_name = 'empresa/one_by_one.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['previous_object'] = prev_in_order(context['empresa'])
        # context['next_object'] = next_in_order(context['empresa'])

        # custom ordering
        emp_id = context['empresa'].id
        com_id = context['empresa'].comercial_id
        qs = models.Empresa.objects.filter(comercial=com_id).order_by('razon_social')
        newest = qs.get(id=emp_id)
        context['previous_object'] = prev_in_order(newest, qs=qs)
        context['next_object'] = next_in_order(newest, qs=qs)

        context['domicilios'] = context['empresa'].domicilios.filter(active=True)
        context['comunicaciones'] = context['empresa'].comunicaciones.filter(active=True)
        context['contactos'] = context['empresa'].contactos.filter(active=True)
        context['actividades'] = context['empresa'].actividades.filter(active=True)
        # context['empresa'].contactos.filter(tipo='movil').filter(active=True)
        # cargamos los celulares de los contactos
        # for reg in context['contactos']:
        #     reg.comunicaciones = reg.comunicaciones.filter(tipo='movil').filter(active=True)
        return context


def buscar_comunicacion(request, pk):
    obj_list = ComunicacionModel.objects.filter(active=True)
    context = {
        'tableID': 'dataTableModal',
        'object_list': obj_list,
        'empresaId': pk,
    }
    return render(request, 'empresa/includes/_modal_comunicacion.html', context)


def asociar_comunicacion(request, empId, comId):
    empresa = models.Empresa.objects.get(id=empId)
    comunicacion = ComunicacionModel.objects.get(id=comId)
    empresa.comunicaciones.add(comunicacion)
    empresa.save()
    return HttpResponseRedirect(reverse('empresa:browse', args=[empId]))


def confirmar_empresa(request, pk):
    object = models.Empresa.objects.get(id=pk)
    object.save()
    messages.success(request, f'Empresa confirmada.')
    return HttpResponseRedirect(reverse('empresa:detail', args=[pk]))
