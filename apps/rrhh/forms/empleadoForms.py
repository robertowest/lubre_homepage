from crispy_forms import bootstrap, helper, layout
from django import forms

from apps.rrhh.models import Empleado





class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['persona', 'legajo', 'fecha_ingreso', 'fecha_egreso', 
                  'imagen', 'tarea', 'usuario', 'active']
        widgets = {
            'fecha_egreso': forms.TextInput(attrs={'placeholder': '30/03/2010'}),
            'fecha_ingreso': forms.TextInput(attrs={'placeholder': '30/03/2010'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # creamos helper
        self.helper = helper.FormHelper()
        self.helper.form_id = "myform"

        # creamos layouts
        self.helper.layout = layout.Layout()

        # agregamos todos los campos
        for fld in self.Meta.fields:
            self.helper.layout.append(fld)

        # agregamos los botones de acción
        bSave = '<button type="submit" class="btn btn-primary btn-icon-split mr-1"><span class="icon text-white-50"><i class="fas fa-save"></i></span><span class="text">Grabar</span></button>'
        bCancel = '<a class="btn btn-warning btn-icon-split" href="{{request.META.HTTP_REFERER}}"><span class="icon text-white-50"><i class="fas fa-undo"></i></span><span class="text text-dark">Cancela</span></a>'
        self.helper.layout.append(layout.HTML("<hr>"))
        self.helper.layout.append(layout.HTML(bSave))
        self.helper.layout.append(layout.HTML(bCancel))


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
