from django_filters import CharFilter, DateFilter, FilterSet, NumberFilter
from crispy_forms import helper, layout
from django.urls import reverse

from apps.rrhh.models import Vacaciones


# class CustomDateFilter(DateFilter):
#     def filter(self, qs, value):
#         if value:
#             filter_lookups = {
#                 "%s__month" % (self.field_name, ): value.month,
#                 "%s__year" % (self.field_name, ): value.year
#             }
#             qs = qs.filter(**filter_lookups)
#         return qs
class MesFilter(NumberFilter):
    def filter(self, qs, value):
        if value:
            filter_lookups = {
                "%s__month" % (self.field_name, ): value
            }
            qs = qs.filter(**filter_lookups)
        return qs


class VacacionesFilter(FilterSet):
    periodo = NumberFilter(lookup_expr='iexact')
    mes = MesFilter(field_name="fecha_inicio", lookup_expr='iexact', label="Mes")

    class Meta:
        model = Vacaciones
        fields = ["empleado", "periodo", "mes", "estado"]


class VacacionesFilterForm(helper.FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'get'

        bFilter = '<button type="submit" class="btn btn-sm btn-primary btn-icon-split mr-1"><span class="icon text-white-50"><i class="fas fa-filter"></i></span><span class="text">Filtrar</span></button>'
        bLimpiar = '<a class="btn btn-sm btn-secondary btn-icon-split" href="' + reverse('vacaciones:listado') + '"><span class="icon text-white-50"><i class="fas fa-undo"></i></span><span class="text">Limpiar</span></a>'

        self.layout = layout.Layout(
            layout.Div(
                layout.Row(
                    layout.Div(
                        layout.Row(
                            layout.Column('empleado', css_class='col-lg-6 col-md-4 col-sm-12 mb-0'),
                            layout.Column('periodo',  css_class='col-lg-2 col-md-3 col-sm-4 mb-0'),
                            layout.Column('mes',      css_class='col-lg-2 col-md-1 col-sm-4 mb-0'),
                            layout.Column('estado',   css_class='col-lg-2 col-md-4 col-sm-4 mb-0'),
                        ),
                        css_class="col-lg-12 col-md-12 col-sm-12",
                    ),
                    layout.Div(
                        layout.HTML(bFilter),
                        layout.HTML(bLimpiar),
                        css_class="col-12 text-right",
                    ),
                )
            )
        )
