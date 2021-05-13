from django.views.generic.edit import CreateView, UpdateView
from .models import Direccion


class DireccionCreateView(CreateView):
    model = Direccion
    fields = ['provincia', 'departamento', 'localidad']


class DireccionUpdateView(UpdateView):
    model = Direccion
    fields = ['provincia', 'departamento', 'localidad']
