import django_tables2 as tables

from apps.empresa.models import Comercial

class ComercialTable(tables.Table):
    class Meta:
        model = Comercial
        template_name = "django_tables2/bootstrap.html"
        fields = ['id', 'persona', 'active']
