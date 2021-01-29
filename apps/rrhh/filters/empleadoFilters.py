from django_filters import FilterSet, CharFilter
from crispy_forms import helper, layout

from apps.rrhh.models import Empleado


class EmpleadoFilter(FilterSet):
    nombre = CharFilter(label='Nombre', lookup_expr='icontains')
    apellido = CharFilter(label='Apellido', lookup_expr='icontains')
    documento = CharFilter(label='DNI', lookup_expr='icontains')

    class Meta:
        model = Empleado
        fields = ['nombre', 'apellido', 'documento', 'active']


class EmpleadoFilterForm(helper.FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'get'

        bFilter = '<button type="submit" class="btn btn-sm btn-primary btn-icon-split mr-1"><span class="icon text-white-50"><i class="fas fa-filter"></i></span><span class="text">Filtrar</span></button>'
        bLimpiar = '<a class="btn btn-sm btn-secondary btn-icon-split" href="/rrhh/empleado/listado/"><span class="icon text-white-50"><i class="fas fa-undo"></i></span><span class="text">Limpiar</span></a>'

        self.layout = layout.Layout(
            layout.Div(
                layout.Row(
                    layout.Div(
                        layout.Row(
                            layout.Column('persona', css_class='col-lg-7 col-md-4 col-sm-12 mb-0'),
                            layout.Column('legajo', css_class='col-lg-3 col-md-4 col-sm-12 mb-0'),
                            layout.Column('active', css_class='col-lg-2 col-md-1 col-sm-3 mb-0'),
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
