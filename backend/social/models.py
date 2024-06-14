from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


class CustomUserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars', default='avatars/guest.png')
    alias = models.CharField(_("alias"), max_length=150, blank=True)

    def __str__(self):
        return self.alias or self.user.username

    def save(self, *args, **kwargs):
        if not self.alias:
            self.alias = self.user.username
        super().save(*args, **kwargs)
