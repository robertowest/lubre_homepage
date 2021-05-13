import django_filters

from .models import Persona


class PersonaFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(label='Nombre', lookup_expr='icontains')
    apellido = django_filters.CharFilter(label='Apellido', lookup_expr='icontains')
    documento = django_filters.CharFilter(label='DNI', lookup_expr='icontains')

    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'documento', 'active']


class PersonaFindFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    apellido = django_filters.CharFilter(lookup_expr='icontains')
    documento = django_filters.CharFilter(label='DNI', lookup_expr='icontains')
    active = django_filters.BooleanFilter(initial=True)

    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'documento', 'active']

    def __init__(self, data=None, *args, **kwargs):
        # valor inicial por defecto para el filtro
        if data is not None:
            data = data.copy()
            data.setdefault('active', True)
        super(PersonaFindFilter, self).__init__(data, *args, **kwargs)
