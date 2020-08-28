import django_tables2 as tables
# from django_tables2 import tables
from django_tables2.utils import A

from .models import Comunicacion


# -------------------------------------------------------------------
# Comunicacion
# -------------------------------------------------------------------
class ComunicacionTable(tables.Table):
    # texto = tables.LinkColumn('comunicacion:detail', text='static text', args=[A('pk')])
    texto = tables.LinkColumn('comunicacion:update', args=[A('pk')])

    class Meta:
        # attrs = {"class": "table table-striped table-hover cabecera-azul"}
        attrs = {"class": "table table-hover"}
        model = Comunicacion
        fields = ['id', 'tipo', 'texto', 'active']
        empty_text = "No hay datos para los criterios de búsqueda."
        template_name = "django_tables2/bootstrap4.html"
        # per_page = 20
