from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class UserProfile(User):
    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'
        
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
        return name

    def get_absolute_url(self):
        # reverse('persona:info', kwargs={'pk': self.pk})
        return reverse('comercial:detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('comercial:update', args=(self.pk,))

    def get_delete_url(self):
        return reverse('comercial:delete', args=(self.pk,))