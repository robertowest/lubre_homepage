from crispy_forms import helper, layout
from django import forms

from apps.rrhh.models import Vacaciones


class VacacionesForm(forms.ModelForm):
    class Meta:
        model = Vacaciones
        fields = ['empleado', 'fecha_inicio', 'fecha_fin', 
                  'fecha_solicitud', 'periodo', 'observacion', 'estado', 'active']
        widgets = {
            'fecha_inicio': forms.TextInput(attrs={'placeholder': '30/03/2010'}),
            'fecha_fin': forms.TextInput(attrs={'placeholder': '30/03/2010'}),
            'fecha_solicitud': forms.TextInput(attrs={'placeholder': '30/03/2010'}),
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
