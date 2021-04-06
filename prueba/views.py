from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render
from django_tables2 import RequestConfig

from apps.comunes.models import Comunicacion
from apps.comunes.filters import ComunicacionFindFilter
from apps.comunes.tables import ComunicacionFindTable
from apps.comunes.forms.comunicacion import ComunicacionFilterFormModal


class ComunicacionTableView(TemplateView):
    template_name = 'prueba/base.html'

    def get_queryset(self, **kwargs):
        return Comunicacion.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ComunicacionTableView, self).get_context_data(**kwargs)
        filter = ComunicacionFindFilter(self.request.GET, queryset=self.get_queryset(**kwargs))
        # if self.request.GET:
        #     filter = ComunicacionFindFilter(self.request.GET, queryset=self.get_queryset(**kwargs))
        # else:
        #     from django.http import QueryDict
        #     qd = QueryDict('tipo=3&texto=?&active=True&submit=Filtrar')
        #     filter = ComunicacionFindFilter(qd, queryset=self.get_queryset(**kwargs))
        filter.form.helper = ComunicacionFilterFormModal()
        table = ComunicacionFindTable(filter.qs[:10])   # solo 10 registros
        RequestConfig(self.request).configure(table)
        context['filter'] = filter
        context['table'] = table
        return context


def comunicacion_table_view(request):
    # # from django.template import Context, Template
    # # t = Template("{% render_table table %}")
    # # c = Context({'filter': filter})
    # # return t.render(c)

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
    return render(request, 'prueba/includes/find_modal_data.html', context)