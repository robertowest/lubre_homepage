from django_filters import FilterSet, CharFilter
from crispy_forms import helper, layout

from apps.rrhh.models import Empleado


class EmpleadoFilter(FilterSet):
    nombre = CharFilter(label='Nombre', lookup_expr='icontains')
    apellido = CharFilter(label='Apellido', lookup_expr='icontains')
    documento = CharFilter(label='DNI', lookup_expr='icontains')

    class Meta:
        model = Empleado
        fields = ['nombre', 'apellido', 'documento', 'active']
