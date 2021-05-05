import django_filters

from .models import Comunicacion, Domicilio


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
            # data.setdefault('id', 0)
            data.setdefault('active', True)
        super(ComunicacionListFilter, self).__init__(data, *args, **kwargs)


# -------------------------------------------------------------------
# Domicilio
# -------------------------------------------------------------------
class DomicilioListFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Domicilio
        fields = ['id', 'nombre', 'active']

    def __init__(self, data=None, *args, **kwargs):
        if data is not None:
            data = data.copy()
            data.setdefault('active', True)
        super(DomicilioListFilter, self).__init__(data, *args, **kwargs)


# -------------------------------------------------------------------
# para buscar elemento en ventana modal
# -------------------------------------------------------------------

class ComunicacionFindFilter(django_filters.FilterSet):
    texto = django_filters.CharFilter(lookup_expr='icontains')
    active = django_filters.BooleanFilter(initial=True)

    class Meta:
        model = Comunicacion
        fields = ['tipo', 'texto', 'active']

    # def __init__(self, data=None, *args, **kwargs):
    #     if self.data == {}:
    #         self.queryset = self.queryset.none()
    #     if data is not None:
    #         data = data.copy()
    #         data.setdefault('tipo', 3)      # Teléfono
    #         data.setdefault('active', True)
    #     super(ComunicacionFindFilter, self).__init__(data, *args, **kwargs)
    def __init__(self, *args, **kwargs):
        super(ComunicacionFindFilter, self).__init__(*args, **kwargs)
        if self.data == {}:
            self.queryset = self.queryset.none()


class DomicilioFindFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    active = django_filters.BooleanFilter(initial=True)

    class Meta:
        model = Domicilio
        fields = ['nombre', 'numero', 'active']

    def __init__(self, *args, **kwargs):
        super(DomicilioFindFilter, self).__init__(*args, **kwargs)
        if self.data == {}:
            self.queryset = self.queryset.none()
