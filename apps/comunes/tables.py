import django_tables2 as tables
from django_tables2.utils import A

from .models import Comunicacion

ACTIONS = '''
<a href="{% url 'comunicacion:detail' record.pk %}" class="text-info" title="" data-toggle="tooltip" data-original-title="View"><i class="fa fa-eye">&nbsp;</i></a>
<a href="{% url 'comunicacion:update' record.pk %}" class="text-primary" title="" data-toggle="tooltip" data-original-title="Edit"><i class="fa fa-edit">&nbsp;</i></a>
<a href="{% url 'comunicacion:delete' record.pk %}?next={{request.get_full_path|urlencode}}" class="text-danger" data-toggle="tooltip" data-original-title="Eliminar"><i class="fa fa-trash">&nbsp;</i></a>
'''
# <a href="{% url 'comunicacion:delete' record.pk %}" class="text-danger" title="" data-toggle="tooltip" data-original-title="Delete"><i class="fa fa-trash">&nbsp;</i></a>
# <a href="{% url 'comunicacion:delete' record.pk %}" class="text-danger"
#     data-toggle="modal" data-target="#confirmDelete"
#     data-title="Eliminar Comunicación"
#     data-message="¿Está seguro de eliminar esta comunicación?"
#     data-url="{% url 'comunicacion:delete' record.pk %}">
#     <i class="fa fa-trash"></i>
# </a>


# -------------------------------------------------------------------
# Comunicacion
# -------------------------------------------------------------------
class ComunicacionTable(tables.Table):
    # texto = tables.LinkColumn('comunicacion:update', args=[A('pk')])
    id = tables.Column(orderable=False)
    tipo = tables.Column(orderable=False)
    texto = tables.Column(orderable=False)
    active = tables.BooleanColumn(orderable=False)
    actions = tables.TemplateColumn(template_code=ACTIONS, verbose_name='Acciones', orderable=False)
    # id = tables.LinkColumn('comunicacion:delete', args=[A('pk')], attrs={'a': {'class': 'btn'}})

    class Meta:
        # attrs = {"class": "table table-striped table-hover cabecera-azul"}
        attrs = {"class": "table table-hover"}
        model = Comunicacion
        fields = ['id', 'tipo', 'texto', 'active']
        sequence = ['id', 'tipo', 'texto', 'active', 'actions']
        empty_text = "No hay datos para los criterios de búsqueda."
        template_name = "django_tables2/bootstrap4.html"
        per_page = 20


class ComunicacionFindTable(tables.Table):
    id = tables.Column(orderable=False)
    tipo = tables.Column(orderable=False)
    # texto = tables.Column(linkify=True, orderable=False)
    # texto = tables.LinkColumn('app:url', args=[A('pk')])
    # texto = tables.TemplateColumn('<a href="{{record.url}}">{{record.name}}</a>')
    texto = tables.TemplateColumn('<a href="#" class="enlace" data-pk="{{record.id}}">{{record.texto}}</a>', orderable=False)
    # active = tables.Column(orderable=False)

    class Meta:
        # attrs = {"class": "table table-striped table-hover cabecera-azul"}
        attrs = {"class": "table table-hover"}
        model = Comunicacion
        fields = ['id', 'tipo', 'texto', 'active']
        empty_text = "No hay datos para los criterios de búsqueda."
        template_name = "django_tables2/bootstrap4.html"
        per_page = 10
