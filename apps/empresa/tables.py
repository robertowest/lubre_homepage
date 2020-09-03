import django_tables2 as tables
from django_tables2.utils import A
from django.utils.translation import gettext_lazy as _

from .models import Empresa

ACTIONS = '''
<a href="{% url 'empresa:detail' record.pk %}" class="text-info" data-toggle="tooltip" data-original-title="Ver"><i class="fa fa-eye">&nbsp;</i></a>
<a href="{% url 'empresa:update' record.pk %}" class="text-primary" data-toggle="tooltip" data-original-title="Editar"><i class="fa fa-edit">&nbsp;</i></a>
<a href="{% url 'empresa:delete' record.pk %}?next={{request.get_full_path|urlencode}}" class="text-danger" data-toggle="tooltip" data-original-title="Eliminar"><i class="fa fa-trash">&nbsp;</i></a>
'''


class EmpresaTable(tables.Table):
    # id = tables.Column(orderable=False)
    # nombre = tables.Column(orderable=False)
    # razon_social = tables.LinkColumn('empresa:update', args=[A('pk')], orderable=True)
    razon_social = tables.Column()
    cuit = tables.Column(orderable=False)
    comercial = tables.Column(orderable=False)
    actividad = tables.Column(orderable=False)
    active = tables.BooleanColumn(orderable=False)
    actions = tables.TemplateColumn(template_code=ACTIONS, verbose_name='Acciones', orderable=False)

    class Meta:
        model = Empresa
        attrs = {"class": "table table-hover"}    # table-striped 
        fields = ['razon_social', 'cuit', 'comercial', 'actividad', 'active']
        sequence = ['razon_social', 'cuit', 'comercial', 'actividad', 'active']
        empty_text = "No hay datos que satisfaga los criterios de búsqueda."
        template_name = "django_tables2/bootstrap4.html"
        per_page = 20
