from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 
                  'first_name', 'last_name', 
                  'is_active', 'is_staff', 'is_superuser'] 
