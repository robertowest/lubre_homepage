import django_tables2 as tables
from django_tables2.utils import A
from django.utils.translation import gettext_lazy as _

from apps.rrhh.models import Denuncia_ART


def _actions_allowed_denuncia_art():
    ACTIONS = '''
    {% if perms.denuncia_art.view_denuncia_art %} 
    <a href="{% url 'denuncia_art:detail' record.pk %}" class="text-info" data-toggle="tooltip" data-original-title="Ver"><i class="fa fa-eye">&nbsp;</i></a>
    {% endif %}

    {% if perms.denuncia_art.change_denuncia_art %} 
    <a href="{% url 'denuncia_art:update' record.pk %}" class="text-primary" data-toggle="tooltip" data-original-title="Editar"><i class="fa fa-edit">&nbsp;</i></a>
    {% endif %}

    {% if perms.denuncia_art.delete_denuncia_art %} 
    <a href="{% url 'denuncia_art:delete' record.pk %}?next={{request.get_full_path|urlencode}}" class="text-danger" data-toggle="tooltip" data-original-title="Eliminar"><i class="fa fa-trash">&nbsp;</i></a>
    {% endif %}
    '''
    return ACTIONS


class DenunciaTable(tables.Table):
    empleado = tables.Column(orderable=True)
    siniestro = tables.Column(orderable=False)
    tipo_accidente = tables.Column(orderable=False)
    estado = tables.Column(orderable=False, verbose_name='Edad')
    active = tables.BooleanColumn(orderable=False)
    actions = tables.TemplateColumn(template_code=_actions_allowed_denuncia_art(), \
                                    verbose_name='Acciones', orderable=False, \
                                    attrs={'th': {'style': 'min-width: 100px;'}})

    class Meta:
        model = Denuncia_ART
        attrs = {"class": "table table-hover"}
        fields = []
        empty_text = "No hay datos que cumplan los criterios de búsqueda."
        template_name = "django_tables2/bootstrap4.html"
        per_page = 20
