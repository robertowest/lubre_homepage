from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

from apps.firebird.models import Clientes


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cuit = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        db_table = "auth_user_profile"

    def __str__(self):
        name = "{} {}".format(self.user.first_name, self.user.last_name).strip()
        if not name:
            name = self.user.username
        return name

    def save(self, *args, **kwargs):
        # # Check how the current values differ from ._loaded_values. For example,
        # # prevent changing the creator_id of the model. (This example doesn't
        # # support cases where 'creator_id' is deferred).
        # if not self._state.adding and (
        #         self.creator_id != self._loaded_values['creator_id']):
        #     raise ValueError("Updating the value of creator isn't allowed")
       
        fcuit = "".join([x for x in self.cuit if x.isdigit()])
        if len(fcuit) == 11:
            fcuit = fcuit[:2] + '-' + fcuit[2:10] + '-' + fcuit[-1:]
            cliente = Clientes.objects.using('firebird').filter(cuit=fcuit)
            if cliente:
                # id = cliente[len(cliente)-1].idcliente
                # si existe un cliente con ese cuit, marcamos el usuario como cliente
                self.cuit = fcuit
            else:
                self.cuit = None
        else:
            self.cuit = None
        super().save(*args, **kwargs)


@receiver(models.signals.post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(models.signals.post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
