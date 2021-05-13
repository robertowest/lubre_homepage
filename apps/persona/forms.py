from crispy_forms import bootstrap, helper, layout
from django import forms
from django.urls import reverse

from .models import Persona


class PersonaForm(forms.ModelForm):
    # active = forms.BooleanField(initial=True)

    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'documento', 'fecha_nacimiento', 'active']
        widgets = {
            'documento': forms.TextInput(attrs={'placeholder': '12.345.678'}),
            'cuit': forms.TextInput(attrs={'placeholder': '20-12345678-9'}),
            'fecha_nacimiento': forms.TextInput(attrs={'placeholder': '30/03/2010'}),
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
        bSave = '<button type="submit" class="btn btn-sm btn-primary btn-icon-split mr-1"><span class="icon text-white-50"><i class="fas fa-save"></i></span><span class="text">Grabar</span></button>'
        bCancel = '<a class="btn btn-sm btn-warning btn-icon-split" href="{{request.META.HTTP_REFERER}}"><span class="icon text-white-50"><i class="fas fa-undo"></i></span><span class="text text-dark">Cancela</span></a>'
        self.helper.layout.append(layout.HTML("<hr>"))
        self.helper.layout.append(layout.HTML(bSave))
        self.helper.layout.append(layout.HTML(bCancel))


class PersonaFilterForm(helper.FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'get'

        bFilter = '<button type="submit" class="btn btn-sm btn-primary btn-icon-split mr-1"><span class="icon text-white-50"><i class="fas fa-filter"></i></span><span class="text">Filtrar</span></button>'
        bLimpiar = '<a class="btn btn-sm btn-secondary btn-icon-split" href="' + reverse('persona:list') + '"><span class="icon text-white-50"><i class="fas fa-undo"></i></span><span class="text">Limpiar</span></a>'

        self.layout = layout.Layout(
            layout.Div(
                layout.Row(
                    layout.Div(
                        layout.Row(
                            layout.Column('nombre', css_class='col-lg-4 col-md-4 col-sm-12 mb-0'),
                            layout.Column('apellido', css_class='col-lg-4 col-md-4 col-sm-12 mb-0'),
                            layout.Column('documento', css_class='col-lg-3 col-md-3 col-sm-6 mb-0'),
                            layout.Column('active', css_class='col-lg-1 col-md-1 col-sm-3 mb-0'),
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


class PersonaFilterFormModal(helper.FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'get'
        self.form_id = 'frmPersona'

        self.layout = layout.Layout(
            layout.Div(
                layout.Fieldset(
                    None,
                    layout.Div(
                        bootstrap.InlineField("nombre", wrapper_class="col-3"),
                        bootstrap.InlineField("apellido", wrapper_class="col-3"),
                        bootstrap.InlineField("documento", wrapper_class="col-3"),
                        bootstrap.InlineField("active", wrapper_class="col-3"),
                        css_class="row",
                    ),
                    css_class="col-10",
                ),
                bootstrap.FormActions(
                    layout.Button('btnFilter', 'Buscar', 
                                  css_id='btnFilter', 
                                  css_class='btn btn-sm btn-primary', 
                                  onclick='submit_modal(frmPersona);'),
                    css_class="col-2 text-right align-self-center",
                ),
                css_class="row",
            )
        )
