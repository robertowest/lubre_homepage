from django.db.models import Q

import django_tables2 as tables

from .models import Persona


class PersonaTable(tables.Table):
    id = tables.Column(linkify=True)
    nombre = tables.Column(order_by=('nombre'))
    documento = tables.Column(orderable=False)
    fecha_nacimiento = tables.Column(orderable=False)
    edad = tables.Column(orderable=False)
    persona_similar = tables.Column(orderable=False)
    # active = tables.Column(orderable=False)
    
    class Meta:
        model = Persona
        template_name = "django_tables2/bootstrap4.html"
        fields = ['id', 'nombre', 'apellido', 'documento', 
                  'fecha_nacimiento', 'edad', 'persona_similar', 
                  'active']
        attrs = {"class": "table table-hover"}
