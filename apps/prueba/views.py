from django.views.generic import DetailView, ListView

from apps.empresa.models import Comercial, Empresa


# from apps.comunes.utils import get_template_path
# template_name = get_template_path(__package__.split('.')[1], "detalle.html")


class PruebaDetailView(DetailView):
    model = Empresa   # .objects.get(id=1511)
    template_name = 'prueba/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# class SearchDataView(ListView):
#     # app = __package__.split('.')[1]         --> lo obtiene de urls.py
#     # app = model._meta.verbose_name.lower()  --> lo obtiene de models.py
#     # template_name = '{app}/index.html'.format(app=__package__.split('.')[1])
#     model = Comercial
#     # template_name = 'prueba/modal_form.html'
#     template_name = 'prueba/tabla_filtro.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['app_name'] = __package__.split('.')[1]
#         # context['object_list'] = Comercial.objects.filter(active=True)
#         return context

#     def get_queryset(self):
#         qs = super().get_queryset()
#         search = self.request.GET.get('search1') 
#         if search:
#             return qs.filter(nombre__icontains=search).filter(active=True)
#         else: 
#             return qs.filter(id=0)


from django_tables2 import SingleTableView
from .tables import ComercialTable


class SearchDataView(SingleTableView):
    model = Comercial   # .objects.filter(active=True)   # .order_by('persona')
    table_class = ComercialTable
    template_name = 'prueba/tabla.html'



from django.shortcuts import render

def comercial1(request):
    table = ComercialTable(Comercial.objects.filter(active=True).order_by('persona'))
    return render(request, 'prueba/tabla.html', {'table': table})
    # filter = ProductFilter(request.GET, queryset=Product.objects.all())
    # return render(request, 'my_app/template.html', {'filter': filter})



from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .filters import ComercialFilter


class comercial2(SingleTableMixin, FilterView):
    model = Comercial   # .objects.filter(active=True).order_by('persona')
    table_class = ComercialTable
    template_name = 'prueba/tabla_filtro.html'
    filterset_class = ComercialFilter


def comercial3(request):
    # model = Comercial
    # table = ComercialTable(Comercial.objects.filter(active=True).order_by('persona'))
    # filter = ComercialFilter(request.GET, queryset=table)
    # return render(request, 'prueba/tabla_filtro.html', {'filter': filter})
    # table = ComercialTable(Comercial.objects.filter(active=True).order_by('persona'))
    # return render(request, 'prueba/tabla_filtro.html', {'table': table})
    f = ComercialFilter(request.GET, queryset=Comercial.objects.filter(active=True).order_by('persona'))
    return render(request, 'prueba/filtro3.html', {'filter': f, 'pk':1511})
