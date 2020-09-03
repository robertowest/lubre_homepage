import django_tables2 as tables
from django_tables2.utils import A
from django.utils.translation import gettext_lazy as _

from .models import Persona

ACTIONS = '''
<a href="{% url 'empresa:detail' record.pk %}" class="text-info" data-toggle="tooltip" data-original-title="Ver"><i class="fa fa-eye">&nbsp;</i></a>
<a href="{% url 'empresa:update' record.pk %}" class="text-primary" data-toggle="tooltip" data-original-title="Editar"><i class="fa fa-edit">&nbsp;</i></a>
<a href="{% url 'empresa:delete' record.pk %}?next={{request.get_full_path|urlencode}}" class="text-danger" data-toggle="tooltip" data-original-title="Eliminar"><i class="fa fa-trash">&nbsp;</i></a>
'''


class PersonaTable(tables.Table):
    # id = tables.Column(linkify=True)
    # nombre = tables.Column(order_by=('nombre'))
    documento = tables.Column(orderable=False)
    fecha_nacimiento = tables.Column(orderable=False)
    edad = tables.Column(orderable=False)
    persona_similar = tables.Column(orderable=False)
    active = tables.BooleanColumn(orderable=False)
    actions = tables.TemplateColumn(template_code=ACTIONS, verbose_name='Acciones', orderable=False)
    
    class Meta:
        model = Persona
        attrs = {"class": "table table-hover"}
        fields = ['nombre', 'apellido', 'documento', 
                  'fecha_nacimiento', 'edad', 'persona_similar', 
                  'active']
        empty_text = "No hay datos que satisfaga los criterios de búsqueda."
        template_name = "django_tables2/bootstrap4.html"
        per_page = 20
