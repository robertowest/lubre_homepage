from django_filters import FilterSet
from crispy_forms import helper, layout

from .models import Persona


class PersonaFilter(FilterSet):
    class Meta:
        model = Persona
        # fields = {'nombre': ['contains'], 'apellido': ['contains'],}
        fields = ['nombre', 'apellido']
