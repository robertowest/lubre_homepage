from django.http import QueryDict
from django.views.generic import TemplateView
from django_tables2 import RequestConfig

from apps.comunes.models import Comunicacion
from apps.comunes.filters import ComunicacionListFilter
from apps.comunes.tables import ComunicacionFindTable
from apps.comunes.forms.comunicacion import ComunicacionFilterFormHelper


class ComunicacionTableView(TemplateView):
    template_name = 'prueba/base.html'

    def get_queryset(self, **kwargs):
        return Comunicacion.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ComunicacionTableView, self).get_context_data(**kwargs)
        filter = ComunicacionListFilter(self.request.GET, queryset=self.get_queryset(**kwargs))
        # if self.request.GET:
        #     filter = ComunicacionListFilter(self.request.GET, queryset=self.get_queryset(**kwargs))
        # else:
        #     qd = QueryDict('id=0&active=True&submit=Filtrar')
        #     filter = ComunicacionListFilter(qd, queryset=self.get_queryset(**kwargs))
        filter.form.helper = ComunicacionFilterFormHelper()
        table = ComunicacionFindTable(filter.qs[:10])   # solo 10 registros
        RequestConfig(self.request).configure(table)
        context['filter'] = filter
        context['table'] = table
        return context