import django_tables2 as tables
from django_tables2.utils import A
from django.contrib.auth.models import Permission, User
from django.utils.translation import gettext_lazy as _

from apps.rrhh.models import Vacaciones


def actions_allowed_vacaciones():
    ACTIONS = '''
    {% if perms.vacaciones.view_vacaciones %} 
    <a href="{% url 'vacaciones:detail' record.pk %}" class="text-info" data-toggle="tooltip" data-original-title="Ver"><i class="fa fa-eye">&nbsp;</i></a>
    {% endif %}

    {% if perms.vacaciones.change_vacaciones %} 
    <a href="{% url 'vacaciones:update' record.pk %}" class="text-primary" data-toggle="tooltip" data-original-title="Editar"><i class="fa fa-edit">&nbsp;</i></a>
    {% endif %}

    {% if perms.vacaciones.delete_vacaciones %} 
    <a href="{% url 'vacaciones:delete' record.pk %}?next={{request.get_full_path|urlencode}}" class="text-danger" data-toggle="tooltip" data-original-title="Eliminar"><i class="fa fa-trash">&nbsp;</i></a>
    {% endif %}
    '''
    return ACTIONS


class VacacionesTable(tables.Table):
    ESTADO = '''
    {% if record.estado == 'A' %}
    <span class="mr-1 far fa-thumbs-up text-success" data-toggle="tooltip" title="Aprobadas"></span>
    {% else %}
    <span class="mr-1 far fa-thumbs-down text-danger" data-toggle="tooltip" title="Pendientes"></span>
    {% endif %}
    '''

    empleado = tables.Column(orderable=True)
    periodo = tables.Column(orderable=False, verbose_name="Período")
    fecha_inicio = tables.DateTimeColumn(format="d M Y", orderable=True, verbose_name="F.Inicio")
    fecha_fin = tables.DateTimeColumn(format="d M Y", orderable=False, verbose_name="F.Fin")
    dias_solicitados = tables.Column(orderable=False, verbose_name="Días")
    estado = tables.TemplateColumn(template_code=ESTADO, orderable=False)
    actions = tables.TemplateColumn(template_code=actions_allowed_vacaciones(), \
                                    verbose_name='Acciones', orderable=False, \
                                    attrs={'th': {'style': 'min-width: 100px;'}})

    class Meta:
        model = Vacaciones
        attrs = {"class": "table table-hover"}
        fields = ["empleado", "periodo", "fecha_inicio", "fecha_fin", "dias_solicitados", "estado"]
        empty_text = "No hay datos que cumplan los criterios de búsqueda."
        template_name = "django_tables2/bootstrap4.html"
        per_page = 20
