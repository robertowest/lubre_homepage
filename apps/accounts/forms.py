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

    def save(self, user=None):
        user_profile = super(UserProfileForm, self).save(commit=False)
        if user:
            user_profile.user = user
        user_profile.save()
        return user_profile
