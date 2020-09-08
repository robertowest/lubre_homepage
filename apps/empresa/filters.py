from django.http import QueryDict
from django_filters import FilterSet, BooleanFilter, CharFilter, ModelChoiceFilter, NumberFilter
from crispy_forms import helper, layout

from .models import Actividad, Comercial, Empresa


class ActividadFilter(FilterSet):
    pass


class ComercialFilter(FilterSet):
    persona__nombre = CharFilter(label='Nombre', lookup_expr='icontains')
    persona__apellido = CharFilter(label='Apellido', lookup_expr='icontains')
    # active = BooleanFilter(name='Activo', lookup_expr='exact', initial=True)

    class Meta:
        model = Comercial
        fields = ['persona__nombre', 'persona__apellido', 'active']

    # def __init__(self, data=None, *args, **kwargs):
    #     # if filterset is bound, use initial values as defaults
    #     if data is not None:
    #         # get a mutable copy of the QueryDict
    #         data = data.copy()

    #         for name, f in self.base_filters.items():
    #             initial = f.extra.get('initial')

    #             # filter param is either missing or empty, use initial as default
    #             if not data.get(name) and initial:
    #                 data[name] = initial

    #     super().__init__(data, *args, **kwargs)


class EmpresaFilter(FilterSet):
    nombre = CharFilter(label='Nombre', lookup_expr='icontains')
    razon_social = CharFilter(label='Razón Social', lookup_expr='icontains')
    cuit = CharFilter(label='C.U.I.T.', lookup_expr='icontains')
    comercial = ModelChoiceFilter(queryset=Comercial.objects.all())  # filter(active=True)
    actividad = ModelChoiceFilter(queryset=Actividad.objects.filter(parent=None))
    referencia_id = NumberFilter(lookup_expr='iexact')

    class Meta:
        model = Empresa
        fields = ['nombre',  'razon_social', 'cuit', \
                  'comercial', 'actividad', \
                  'referencia_id', 'active']
