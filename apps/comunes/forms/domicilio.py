from crispy_forms import helper, layout
from django import forms


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

        # creamos layouts personalizado
        self.helper.layout = layout.Layout(
            layout.Row(
                layout.Column('tipo', css_class='col-lg-4 col-md-6 mb-0'),
                # layout.Column('active', css_class='col-lg-2 col-md-2 mt-5'),
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
        bSave = '<button type="submit" class="btn btn-primary btn-icon-split"><span class="icon text-white-50"><i class="fas fa-save"></i></span><span class="text">Grabar</span></button>'
        bCancel = '<a class="btn btn-warning btn-icon-split" style="margin-left: 5px" href="{{request.META.HTTP_REFERER}}"><span class="icon text-white-50"><i class="fas fa-undo"></i></span><span class="text">Cancela</span></a>'
        self.helper.layout.append(layout.HTML("<hr>"))
        self.helper.layout.append(layout.HTML(bSave))
        self.helper.layout.append(layout.HTML(bCancel))
