import django_tables2 as tables
from django_tables2.utils import A
from django.contrib.auth.models import Permission, User
from django.utils.translation import gettext_lazy as _

from .models import Persona


def actions_allowed_persona():
    ACTIONS = '''
    {% if perms.persona.view_persona %} 
    <a href="{% url 'persona:detail' record.pk %}" class="text-info" data-toggle="tooltip" data-original-title="Ver"><i class="fa fa-eye">&nbsp;</i></a>
    {% endif %}

    {% if perms.persona.change_persona %} 
    <a href="{% url 'persona:update' record.pk %}" class="text-primary" data-toggle="tooltip" data-original-title="Editar"><i class="fa fa-edit">&nbsp;</i></a>
    {% endif %}

    {% if perms.persona.delete_persona %} 
    <a href="{% url 'persona:delete' record.pk %}?next={{request.get_full_path|urlencode}}" class="text-danger" data-toggle="tooltip" data-original-title="Eliminar"><i class="fa fa-trash">&nbsp;</i></a>
    {% endif %}
    '''
    return ACTIONS


class PersonaTable(tables.Table):
    id = tables.Column(orderable=False)    # (linkify=True)
    # nombre = tables.Column(order_by=('nombre'))
    documento = tables.Column(orderable=False)
    fecha_nacimiento = tables.Column(orderable=False)
    edad = tables.Column(orderable=False)
    persona_similar = tables.Column(orderable=False)
    active = tables.BooleanColumn(orderable=False)
    actions = tables.TemplateColumn(template_code=actions_allowed_persona(), \
                                    verbose_name='Acciones', orderable=False, \
                                    attrs={'th': {'style': 'min-width: 100px;'}})
    class Meta:
        model = Persona
        attrs = {"class": "table table-hover"}
        fields = ['id', 'nombre', 'apellido', 'documento', 
                  'fecha_nacimiento', 'edad', 'persona_similar', 
                  'active']
        empty_text = "No hay datos que cumplan los criterios de búsqueda."
        template_name = "django_tables2/bootstrap4.html"
        per_page = 20
