import django_tables2 as tables
from django_tables2.utils import A
from django.utils.translation import gettext_lazy as _

from .models import Empresa

ACTIONS = '''
<a href="{% url 'empresa:detail' record.pk %}" class="text-info" title="" data-toggle="tooltip" data-original-title="View"><i class="fa fa-eye">&nbsp;</i></a>
<a href="{% url 'empresa:update' record.pk %}" class="text-primary" title="" data-toggle="tooltip" data-original-title="Edit"><i class="fa fa-edit">&nbsp;</i></a>
'''
# <a href="{% url 'empresa:delete' record.pk %}" class="text-danger" title="" data-toggle="tooltip" data-original-title="Delete"><i class="fa fa-trash">&nbsp;</i></a>


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