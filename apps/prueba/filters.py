import django_filters

from apps.empresa.models import Comercial

class ComercialFilter(django_filters.FilterSet):
    # persona = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Comercial
        fields = ['persona']
