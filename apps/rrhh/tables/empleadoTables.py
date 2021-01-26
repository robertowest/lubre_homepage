import django_tables2 as tables
from django_tables2.utils import A
from django.contrib.auth.models import Permission, User
from django.utils.translation import gettext_lazy as _

from apps.rrhh.models import Empleado


def actions_allowed_empleado():
    ACTIONS = '''
    {% if perms.empleado.view_empleado %} 
    <a href="{% url 'empleado:detail' record.pk %}" class="text-info" data-toggle="tooltip" data-original-title="Ver"><i class="fa fa-eye">&nbsp;</i></a>
    {% endif %}

    {% if perms.empleado.change_empleado %} 
    <a href="{% url 'empleado:update' record.pk %}" class="text-primary" data-toggle="tooltip" data-original-title="Editar"><i class="fa fa-edit">&nbsp;</i></a>
    {% endif %}

    {% if perms.empleado.delete_empleado %} 
    <a href="{% url 'empleado:delete' record.pk %}?next={{request.get_full_path|urlencode}}" class="text-danger" data-toggle="tooltip" data-original-title="Eliminar"><i class="fa fa-trash">&nbsp;</i></a>
    {% endif %}
    '''
    return ACTIONS


class EmpleadoTable(tables.Table):
    persona = tables.Column(orderable=False)
    legajo = tables.Column(orderable=False)
    usuario = tables.Column(orderable=False)
    anio = tables.Column(orderable=False, verbose_name='Edad')
    active = tables.BooleanColumn(orderable=False)
    actions = tables.TemplateColumn(template_code=actions_allowed_empleado(), \
                                    verbose_name='Acciones', orderable=False, \
                                    attrs={'th': {'style': 'min-width: 100px;'}})
    class Meta:
        model = Empleado
        attrs = {"class": "table table-hover"}
        fields = ['persona', 'legajo', 'usuario', 'anio', 'active']
        empty_text = "No hay datos que satisfaga los criterios de búsqueda."
        template_name = "django_tables2/bootstrap4.html"
        per_page = 20
