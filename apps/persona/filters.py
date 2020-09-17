from django_filters import FilterSet, CharFilter
from crispy_forms import helper, layout

from .models import Persona


class PersonaFilter(FilterSet):
    nombre = CharFilter(label='Nombre', lookup_expr='icontains')
    apellido = CharFilter(label='Apellido', lookup_expr='icontains')
    documento = CharFilter(label='DNI', lookup_expr='icontains')

    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'documento', 'active']
