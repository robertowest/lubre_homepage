from django.views import generic

from apps.comunes.utils import get_template_path
from apps.empresa.models import Empresa


class PruebaDetailView(generic.DetailView):
    model = Empresa   # .objects.get(id=1511)
    template_name = get_template_path(__package__.split('.')[1], "detalle.html")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
