from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class UserProfile(User):
    class Meta:
        verbose_name = 'Perfil de Usuario'
        verbose_name_plural = 'Perfíl de Usuarios'
        
    def __str__(self):
        name = ''
        if self.first_name:
            name = self.first_name
        if self.last_name:
            if name:
                name += ' ' + self.last_name
            else:
                name = self.last_name
        if name is None:
            name = self.username
        return 'name'
