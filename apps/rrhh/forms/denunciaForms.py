from crispy_forms import helper, layout
from django import forms

from apps.rrhh.models import Denuncia_ART


class DenunciaForm(forms.ModelForm):
    class Meta:
        model = Denuncia_ART
        fields = ['empleado', 'siniestro', 'fec_siniestro', 'fec_denuncia', 
                  'tipo_accidente', 'tipologia', 'zona_afectada', 'estado', 
                  'fec_alta_medica', 'motivo_alta', 'active']
        widgets = {
            'fec_siniestro': forms.TextInput(attrs={'placeholder': '30/03/2010'}),
            'fec_denuncia': forms.TextInput(attrs={'placeholder': '30/03/2010'}),
            'fec_alta_medica': forms.TextInput(attrs={'placeholder': '30/03/2010'}),
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
