from crispy_forms import helper, layout
from crispy_forms.layout import Submit, Button
from django import forms
from django.contrib.auth.models import User

from .models import UserProfile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 
                  'first_name', 'last_name', 
                  'is_active', 'is_staff', 'is_superuser'] 


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['cuit']

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

        # separador
        self.helper.layout.append(layout.HTML("<hr>"))
        
        # # agregamos los botones de acción
        # bSave = '<button type="submit" class="btn btn-primary btn-icon-split"><span class="icon text-white-50"><i class="fas fa-save"></i></span><span class="text">Grabar</span></button>'
        # bCancel = '<a class="btn btn-warning btn-icon-split" style="margin-left: 5px" href="{{request.META.HTTP_REFERER}}"><span class="icon text-white-50"><i class="fas fa-undo"></i></span><span class="text">Cancela</span></a>'
        # self.helper.layout.append(layout.HTML(bSave))
        # self.helper.layout.append(layout.HTML(bCancel))

        # el botón cancel utiliza el historial del navegador
        self.helper.layout.append(Submit('submit', 'Grabar'))
        self.helper.layout.append(Button('cancel', 'Cancelar',
                                         css_class='btn-default',
                                         onclick="window.history.back()"))

    def save(self, user=None):
        user_profile = super(UserProfileForm, self).save(commit=False)
        if user:
            user_profile.user = user
        user_profile.save()
        return user_profile

    def validate(self, value):
        super().validate(value)
