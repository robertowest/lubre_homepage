from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# one to one relationship
from django.dispatch import receiver


class Profile(models.Model):
    # CASCADE means if the user is deleted the profile is deleted
    # However, If the profile is deleted, the user is not deleted.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(default='img/user_none.jpg', upload_to='profile_pics')
    cuit = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        verbose_name = 'Perfil de Usuario'
        verbose_name_plural = 'Perfíl de Usuarios'
        db_table = "auth_user_profile"

    def __str__(self):
        name = ''
        if self.user.first_name:
            name = self.user.first_name
        if self.user.last_name:
            if name:
                name += ' ' + self.user.last_name
            else:
                name = self.user.last_name
        if name is None:
            name = self.user.username
        return name

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        # image = Image.open(self.image.path)
        # # To resize the profile image
        # if image.height > 400 or image.width > 400:
        #     output_size = (400, 400)
        #     image.thumbnail(output_size)
        #     image.save(self.image.path)

        # modificación del CUIT
        # fcuit = "".join([x for x in self.cuit if x.isdigit()])
        # if len(fcuit) == 11:
        #     fcuit = fcuit[:2] + '-' + fcuit[2:10] + '-' + fcuit[-1:]
        #     cliente = Clientes.objects.using('firebird').filter(cuit=fcuit)
        #     if cliente:
        #         # id = cliente[len(cliente)-1].idcliente
        #         # si existe un cliente con ese cuit, marcamos el usuario como cliente
        #         self.cuit = fcuit
        #     else:
        #         self.cuit = None
        # else:
        #     self.cuit = None
        # super().save(*args, **kwargs)


@receiver(models.signals.post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, imagen=None, cuit=None)


@receiver(models.signals.post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
