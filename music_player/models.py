from django.db import models
from django.contrib.auth.models import AbstractUser


class UserNew(AbstractUser):
    username = models.CharField(max_length=150, unique=True, verbose_name='Username')
    first_login = models.DateTimeField(null=True, verbose_name='First login date')
    custom_url = models.CharField(max_length=24, unique=True, blank=True, null=True, verbose_name='Custom user URL')
    displayName = models.CharField(max_length=24, blank=True, null=True, verbose_name='Display Name')

    def save(self, *args, **kwargs):
        if not self.displayName:
            self.displayName = self.username
        super(UserNew, self).save(*args, **kwargs)