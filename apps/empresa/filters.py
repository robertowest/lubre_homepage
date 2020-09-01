from django_filters import FilterSet, CharFilter, ModelChoiceFilter, NumberFilter
from crispy_forms import helper, layout

from .models import Empresa, Comercial


class EmpresaFilter(FilterSet):
    nombre = CharFilter(label='Nombre', lookup_expr='icontains')
    razon_social = CharFilter(label='Razón Social', lookup_expr='icontains')
    cuit = CharFilter(label='C.U.I.T.', lookup_expr='icontains')
    comercial = ModelChoiceFilter(queryset=Comercial.objects.filter(active=True))
    referencia_id = NumberFilter(lookup_expr='iexact')

    class Meta:
        model = Empresa
        fields = ['nombre',  'razon_social', 'cuit', 'comercial', 'referencia_id', 'active']
