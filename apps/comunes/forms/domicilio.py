from crispy_forms import bootstrap, helper, layout
from django import forms
from django.urls import reverse

from apps.comunes.models import Departamento, Domicilio, Localidad, Provincia


class DomicilioForm(forms.ModelForm):
    class Meta:
        model = Domicilio
        fields = ['tipo', 
                  'tipo_calle', 'nombre', 'numero', 
                  'piso', 'puerta', 'barrio', 
                  'provincia', 'departamento', 'localidad', 
                  'provincia_texto', 'departamento_texto', 'localidad_texto', 
                  'observacion_texto',
                  'active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # # dropdown
        # if self.instance:
        #     if self.instance.provincia_id:
        #         self.fields['departamento'].queryset = (Departamento.objects.filter(provincia_id=self.instance.provincia_id))
        #     if self.instance.departamento_id:
        #         self.fields['localidad'].queryset = (Localidad.objects.filter(departamento_id=self.instance.departamento_id))
        if self.instance.provincia_id:
            self.fields['departamento'].queryset = (Departamento.objects.filter(provincia_id=self.instance.provincia_id))
        if self.instance.departamento_id:
            self.fields['localidad'].queryset = (Localidad.objects.filter(departamento_id=self.instance.departamento_id))

        # creamos helper
        self.helper = helper.FormHelper()
        self.helper.form_id = "myform"

        # # creamos layouts
        # self.helper.layout = layout.Layout()

        # # agregamos todos los campos
        # for fld in self.Meta.fields:
        #     self.helper.layout.append(fld)

        campo = '<div class="formColumn col-lg-1 col-md-2 col-sm-6 mb-0"><div id="div_id_hectarea" class="form-group" style="display: none"><label for="id_hectarea" class="col-form-label">Hectareas</label><div class=""><input type="text" name="hectarea" maxlength="2" class="textinput textInput form-control" id="id_hectarea"></div></div></div>'

        # creamos layouts personalizado
        self.helper.layout = layout.Layout(
            layout.Row(
                layout.Column('tipo', css_class='col-lg-4 col-md-6 mb-0'),
                layout.HTML(campo),
            ),
            layout.Row(
                layout.Column('tipo_calle', css_class='col-lg-3 col-md-6 mb-0'),
                layout.Column('nombre',     css_class='col-lg-6 col-md-9 mb-0'),
                layout.Column('numero',     css_class='col-lg-3 col-md-3 mb-0'),
            ),
            layout.Row(
                layout.Column('piso',   css_class='col-lg-4 col-md-4 col-sm-6 mb-0'),
                layout.Column('puerta', css_class='col-lg-4 col-md-4 col-sm-6 mb-0'),
                layout.Column('barrio', css_class='col-lg-4 col-md-4 col-sm-12 mb-0'),
            ),
            layout.Row(                
                layout.Column('provincia',    css_class='col-lg-4 col-md-6  col-sm-12 mb-0'),
                layout.Column('departamento', css_class='col-lg-4 col-md-6  col-sm-12 mb-0'),
                layout.Column('localidad',    css_class='col-lg-4 col-md-12 col-sm-12 mb-0'),
            ),
            layout.Row(                
                layout.Column(layout.Field('provincia_texto',    readonly=True), css_class='col-lg-4 col-md-12 col-sm-12 mb-0'),
                layout.Column(layout.Field('departamento_texto', readonly=True), css_class='col-lg-4 col-md-12 col-sm-12 mb-0'),
                layout.Column(layout.Field('localidad_texto',    readonly=True), css_class='col-lg-4 col-md-12 col-sm-12 mb-0'),
            ),
            'observacion_texto',
            'active',
        )

        # agregamos los botones de acción
        bSave = '<button type="submit" class="btn btn-sm btn-primary btn-icon-split mr-1"><span class="icon text-white-50"><i class="fas fa-save"></i></span><span class="text">Grabar</span></button>'
        bCancel = '<a class="btn btn-sm btn-warning btn-icon-split" href="{{request.META.HTTP_REFERER}}"><span class="icon text-white-50"><i class="fas fa-undo"></i></span><span class="text text-dark">Cancela</span></a>'
        self.helper.layout.append(layout.HTML("<hr>"))
        self.helper.layout.append(layout.HTML(bSave))
        self.helper.layout.append(layout.HTML(bCancel))


class DomicilioFilterFormHelper_OLD(helper.FormHelper):
    form_class = "form form-inline"
    form_id = "domicilio-search-form"
    form_method = "GET"
    form_tag = True
    html5_required = True
    layout = layout.Layout(
        layout.Div(
            layout.Fieldset(
                "<span class='fa fa-search'></span> Búsqueda de Domicilios",
                layout.Div(
                    bootstrap.InlineField("id", wrapper_class="col-2"),
                    bootstrap.InlineField("nombre", wrapper_class="col-8"),
                    bootstrap.InlineField("active", wrapper_class="col-2"),
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


class DomicilioFilterFormHelper(helper.FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'get'

        bFilter = '<button type="submit" class="btn btn-sm btn-primary btn-icon-split mr-1"><span class="icon text-white-50"><i class="fas fa-filter"></i></span><span class="text">Filtrar</span></button>'
        bLimpiar = '<a class="btn btn-sm btn-secondary btn-icon-split" href="' + reverse('domicilio:list') + '"><span class="icon text-white-50"><i class="fas fa-undo"></i></span><span class="text">Limpiar</span></a>'

        self.layout = layout.Layout(
            layout.Div(
                layout.Row(
                    layout.Div(
                        layout.Row(
                            layout.Column('nombre', css_class='col-lg-10 col-md-10 col-sm-9 mb-0'),
                            layout.Column('active', css_class='col-lg-2  col-md-2  col-sm-3 mb-0'),
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


class DomicilioFilterFormModal(helper.FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'get'
        self.form_id = 'frmDomicilio'

        self.layout = layout.Layout(
            layout.Div(
                layout.Fieldset(
                    None,
                    layout.Div(
                        bootstrap.InlineField("nombre", wrapper_class="col-5"),
                        bootstrap.InlineField("numero", wrapper_class="col-4"),
                        bootstrap.InlineField("active", wrapper_class="col-3"),
                        css_class="row",
                    ),
                    css_class="col-10",
                ),
                bootstrap.FormActions(
                    # layout.Submit("submit", "Buscar", css_id="btnBuscar"),
                    layout.Button('btnFilter', 'Buscar', 
                                  css_id='btnFilter', 
                                  css_class='btn btn-sm btn-primary', 
                                  onclick='submit_modal(frmDomicilio);'),
                    css_class="col-2 text-right align-self-center",
                ),
                css_class="row",
            )
        )
