from crispy_forms import bootstrap, helper, layout
from django import forms

from .models import Persona


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'documento', 'fecha_nacimiento', 'active']
        widgets = {
            'documento': forms.TextInput(attrs={'placeholder': '20.123.456'}),
            'fecha_nacimiento': forms.TextInput(attrs={'placeholder': '31/03/1990'}),
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
        bSave = '<button type="submit" class="btn btn-primary btn-icon-split"><span class="icon text-white-50"><i class="fas fa-save"></i></span><span class="text">Grabar</span></button>'
        bCancel = '<a class="btn btn-warning btn-icon-split" style="margin-left: 5px" href="{{request.META.HTTP_REFERER}}"><span class="icon text-white-50"><i class="fas fa-undo"></i></span><span class="text">Cancela</span></a>'
        self.helper.layout.append(layout.HTML("<hr>"))
        self.helper.layout.append(layout.HTML(bSave))
        self.helper.layout.append(layout.HTML(bCancel))


class PersonaFilterForm(helper.FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'get'

        bFilter = '<button type="submit" class="btn btn-primary btn-icon-split"><span class="icon text-white-50"><i class="fas fa-filter"></i></span><span class="text">Filtrar</span></button>'
        bLimpiar = '<a class="btn btn-secondary btn-icon-split" style="margin-left: 5px" href="/persona/listado/"><span class="icon text-white-50"><i class="fas fa-undo"></i></span><span class="text">Limpiar</span></a>'

        self.layout = layout.Layout(
            layout.Div(
                layout.Row(
                    layout.Div(
                        layout.Row(
                            layout.Column('nombre', css_class='col-lg-4 col-md-4 col-sm-12 mb-0'),
                            layout.Column('apellido', css_class='col-lg-4 col-md-4 col-sm-12 mb-0'),
                            layout.Column('documento', css_class='col-lg-4 col-md-4 col-sm-6 mb-0'),
                        ),
                        css_class="col-lg-10 col-md-12 col-sm-12",
                    ),
                    layout.Div(
                        layout.HTML(bFilter),
                        layout.HTML(bLimpiar),
                        css_class="col-lg-2 text-right",
                    ),
                )
            )
        )
