from django_filters import FilterSet, CharFilter

from apps.empresa.models import Comercial


class ComercialFilter(FilterSet):
    # lookup_expr='icontains'
    # lookup_expr='iexact'
    # lookup_expr='gt'
    # lookup_expr='lt'
    # persona = CharFilter(lookup_expr='icontains')
    persona__nombre = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Comercial
        # fields = ['persona__nombre', 'persona__apellido']
        fields = ['persona__nombre']
