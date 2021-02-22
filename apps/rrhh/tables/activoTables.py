import django_tables2 as tables
from django_tables2.utils import A
from django.utils.translation import gettext_lazy as _

from apps.rrhh.models import Activo


def _actions_allowed_activo():
    ACTIONS = '''
    {% if perms.activo.view_activo %} 
    <a href="{% url 'activo:detail' record.pk %}" class="text-info" data-toggle="tooltip" data-original-title="Ver"><i class="fa fa-eye">&nbsp;</i></a>
    {% endif %}

    {% if perms.activo.change_activo %} 
    <a href="{% url 'activo:update' record.pk %}" class="text-primary" data-toggle="tooltip" data-original-title="Editar"><i class="fa fa-edit">&nbsp;</i></a>
    {% endif %}

    {% if perms.activo.delete_activo %} 
    <a href="{% url 'activo:delete' record.pk %}?next={{request.get_full_path|urlencode}}" class="text-danger" data-toggle="tooltip" data-original-title="Eliminar"><i class="fa fa-trash">&nbsp;</i></a>
    {% endif %}
    '''
    return ACTIONS


class ActivoTable(tables.Table):
    tipo = tables.Column(orderable=False)
    descripcion = tables.Column(orderable=False)
    responsable = tables.Column(orderable=True)
    active = tables.BooleanColumn(orderable=False)
    actions = tables.TemplateColumn(template_code=_actions_allowed_activo(), \
                                    verbose_name='Acciones', orderable=False, \
                                    attrs={'th': {'style': 'min-width: 100px;'}})

    class Meta:
        model = Activo
        attrs = {"class": "table table-hover"}
        fields = []
        empty_text = "No hay datos que cumplan los criterios de búsqueda."
        template_name = "django_tables2/bootstrap4.html"
        per_page = 20
