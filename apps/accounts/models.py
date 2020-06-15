from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.urls import reverse


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


@receiver(models.signals.post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


# @receiver(models.signals.post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.userprofile.save()
