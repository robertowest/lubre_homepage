from crispy_forms import helper, layout
from django import forms

from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 
                  'first_name', 'last_name', 
                  'is_active', 'is_staff', 'is_superuser'] 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # creamos helper
        self.helper = helper.FormHelper()
        self.helper.form_id = "myform"

        # creamos layouts
        self.helper.layout = layout.Layout()        

        # # agregamos todos los campos
        # for fld in self.Meta.fields:
        #     self.helper.layout.append(fld)

        # creamos layouts personalizado
        self.helper.layout = layout.Layout(
            'username',
            'email',
            layout.Row(
                layout.Column('first_name', css_class='col-lg-6 col-md-12 mb-0'),
                layout.Column('last_name'),
            ),
            'is_active',
            'is_staff',
            'is_superuser',
        )            

        # agregamos los botones de acción
        bSave = '<button type="submit" class="btn btn-primary btn-icon-split"><span class="icon text-white-50"><i class="fas fa-save"></i></span><span class="text">Grabar</span></button>'
        bCancel = '<a class="btn btn-warning btn-icon-split" style="margin-left: 5px" href="{{request.META.HTTP_REFERER}}"><span class="icon text-white-50"><i class="fas fa-undo"></i></span><span class="text">Cancela</span></a>'
        self.helper.layout.append(layout.HTML("<hr>"))
        self.helper.layout.append(layout.HTML(bSave))
        self.helper.layout.append(layout.HTML(bCancel))
