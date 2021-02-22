import django_tables2 as tables
from django_tables2.utils import A
from django.utils.translation import gettext_lazy as _

from .models import Actividad, Comercial, Empresa

# min-width: 100px;
# name = tables.Column(attrs={"th": {"id": "foo"}})

def actions_allowed_comercial():
    # href="{% url ...%}?next={{request.get_full_path|urlencode}}"
    # request.GET.next

    ACTIONS = '''
    {% if perms.empresa.view_actividad %} 
    <a href="{% url 'actividad:detail' record.pk %}" class="text-info" data-toggle="tooltip" data-original-title="Ver"><i class="fa fa-eye">&nbsp;</i></a>
    {% endif %}

    {% if perms.empresa.change_actividad %} 
    <a href="{% url 'actividad:update' record.pk %}" class="text-primary" data-toggle="tooltip" data-original-title="Editar"><i class="fa fa-edit">&nbsp;</i></a>
    {% endif %}

    {% if perms.empresa.delete_actividad %} 
    <a href="{% url 'actividad:delete' record.pk %}?next={{request.get_full_path|urlencode}}" class="text-danger" data-toggle="tooltip" data-original-title="Eliminar"><i class="fa fa-trash">&nbsp;</i></a>
    {% endif %}
    '''
    return ACTIONS

class ActividadTable(tables.Table):
    nombre = tables.Column()
    parent = tables.Column(orderable=False)
    active = tables.BooleanColumn(orderable=False)
    actions = tables.TemplateColumn(template_code=actions_allowed_comercial(), \
                                    verbose_name='Acciones', orderable=False, \
                                    attrs={'th': {'style': 'min-width: 100px;'}})
    class Meta:
        model = Actividad
        attrs = {"class": "table table-hover"}
        fields = ['nombre', 'parent', 'active']
        empty_text = "No hay datos que cumplan los criterios de búsqueda."
        template_name = "django_tables2/bootstrap4.html"
        per_page = 100


def actions_allowed_comercial():
    ACTIONS = '''
    {% if perms.empresa.view_comercial %} 
    <a href="{% url 'comercial:detail' record.pk %}" class="text-info" data-toggle="tooltip" data-original-title="Ver"><i class="fa fa-eye">&nbsp;</i></a>
    {% endif %}

    {% if perms.empresa.change_comercial %} 
    <a href="{% url 'comercial:update' record.pk %}" class="text-primary" data-toggle="tooltip" data-original-title="Editar"><i class="fa fa-edit">&nbsp;</i></a>
    {% endif %}

    {% if perms.empresa.delete_comercial %} 
    <a href="{% url 'comercial:delete' record.pk %}?next={{request.get_full_path|urlencode}}" class="text-danger" data-toggle="tooltip" data-original-title="Eliminar"><i class="fa fa-trash">&nbsp;</i></a>
    {% endif %}
    '''
    return ACTIONS


class ComercialTable(tables.Table):
    # id = tables.Column(orderable=False)
    # nombre = tables.Column(orderable=False)
    # razon_social = tables.LinkColumn('comercial:update', args=[A('pk')], orderable=True)
    persona = tables.Column()
    usuario = tables.Column(orderable=False)
    active = tables.BooleanColumn(orderable=False)
    actions = tables.TemplateColumn(template_code=actions_allowed_comercial(), \
                                    verbose_name='Acciones', orderable=False, \
                                    attrs={'th': {'style': 'min-width: 100px;'}})
    class Meta:
        model = Comercial
        attrs = {"class": "table table-hover"}    # table-striped 
        fields = ['persona', 'usuario', 'active']
        # sequence = []
        empty_text = "No hay datos que cumplan los criterios de búsqueda."
        template_name = "django_tables2/bootstrap4.html"
        per_page = 20


def actions_allowed_empresa():
    ACTIONS = '''
    {% if perms.empresa.view_empresa %} 
    <a href="{% url 'empresa:detail' record.pk %}" class="text-info" data-toggle="tooltip" data-original-title="Ver"><i class="fa fa-eye">&nbsp;</i></a>
    {% endif %}

    {% if perms.empresa.change_empresa %} 
    <a href="{% url 'empresa:update' record.pk %}" class="text-primary" data-toggle="tooltip" data-original-title="Editar"><i class="fa fa-edit">&nbsp;</i></a>
    {% endif %}

    {% if perms.empresa.delete_empresa %} 
    <a href="{% url 'empresa:delete' record.pk %}?next={{request.get_full_path|urlencode}}" class="text-danger" data-toggle="tooltip" data-original-title="Eliminar"><i class="fa fa-trash">&nbsp;</i></a>
    {% endif %}
    '''
    return ACTIONS


class EmpresaTable(tables.Table):
    # id = tables.Column(orderable=False)
    nombre = tables.Column()
    # razon_social = tables.LinkColumn('empresa:update', args=[A('pk')], orderable=True)
    # razon_social = tables.Column()
    cuit = tables.Column(orderable=False)
    # comercial = tables.Column(orderable=False)
    # actividad = tables.Column(orderable=False)
    active = tables.BooleanColumn(orderable=False)
    modified = tables.DateColumn(orderable=True)
    actions = tables.TemplateColumn(template_code=actions_allowed_empresa(), \
                                    verbose_name='Acciones', orderable=False, \
                                    attrs={'th': {'style': 'min-width: 100px;'}})

    class Meta:
        model = Empresa
        attrs = {"class": "table table-hover"}    # table-striped 
        fields = ['nombre', 'cuit', 'modified', 'active']
        # sequence = ['nombre', 'cuit', 'comercial', 'actividad', 'active']
        empty_text = "No hay datos que cumplan los criterios de búsqueda."
        template_name = "django_tables2/bootstrap4.html"
        per_page = 20
