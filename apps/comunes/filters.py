import django_filters

from .models import Comunicacion


# -------------------------------------------------------------------
# Comunicacion
# -------------------------------------------------------------------
class ComunicacionListFilter(django_filters.FilterSet):
    # id = django_filters.NumberFilter(lookup_expr='iexact', initial=0)
    texto = django_filters.CharFilter(lookup_expr='icontains')
    # active = django_filters.BooleanFilter(initial=True)

    class Meta:
        model = Comunicacion
        fields = ['id', 'tipo', 'texto', 'active']

    def __init__(self, data=None, *args, **kwargs):
        if data is not None:
            data = data.copy()
            data.setdefault('id', 0)
            data.setdefault('active', True)
        super(ComunicacionListFilter, self).__init__(data, *args, **kwargs)


# -------------------------------------------------------------------
# para buscar elemento en ventana modal
# -------------------------------------------------------------------
class ComunicacionFindFilter(django_filters.FilterSet):
    texto = django_filters.CharFilter(lookup_expr='icontains')
    active = django_filters.BooleanFilter(initial=True)

    class Meta:
        model = Comunicacion
        fields = ['tipo', 'texto', 'active']

    def __init__(self, data=None, *args, **kwargs):
        if data is not None:
            data = data.copy()
            data.setdefault('tipo', 3)      # Teléfono
            data.setdefault('active', True)
        super(ComunicacionFindFilter, self).__init__(data, *args, **kwargs)
