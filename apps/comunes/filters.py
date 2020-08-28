import django_filters

from .models import Comunicacion


# -------------------------------------------------------------------
# Comunicacion
# -------------------------------------------------------------------
class ComunicacionListFilter(django_filters.FilterSet):
    # id = django_filters.NumberFilter(lookup_expr='iexact')
    texto = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Comunicacion
        fields = ['id', 'tipo', 'texto']
