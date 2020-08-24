import django_tables2 as tables

from apps.empresa.models import Comercial


class ComercialTable(tables.Table):
    # id = tables.Column()
    # active = tables.Column()
    class Meta:
        model = Comercial
        template_name = "django_tables2/bootstrap.html"
        fields = ('persona', 'active')