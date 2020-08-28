from crispy_forms import bootstrap, helper, layout
from django import forms

from apps.comunes.models import Comunicacion as ComunicacionModel


class ComunicacionForm(forms.ModelForm):
    class Meta:
        model = ComunicacionModel
        fields = ['tipo', 'texto', 'active']

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


class ComunicacionFilterFormHelper(helper.FormHelper):
    form_class = "form form-inline"
    form_id = "comunicacion-search-form"
    form_method = "GET"
    form_tag = True
    html5_required = True
    layout = layout.Layout(
        layout.Div(
            layout.Fieldset(
                "<span class='fa fa-search'></span> Búsqueda de Comunicaciones",
                layout.Div(
                    bootstrap.InlineField("id", wrapper_class="col-4"),
                    bootstrap.InlineField("tipo", wrapper_class="col-4"),
                    bootstrap.InlineField("texto", wrapper_class="col-4"),
                    css_class="row",
                ),
                css_class="col-11 border p-3",
            ),
            bootstrap.FormActions(
                layout.Submit("submit", "Filtrar"),
                css_class="col-1 text-right align-self-center",
            ),
            css_class="row",
        )
    )
