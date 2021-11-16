from django.db import models
from django.conf import settings
import django.contrib.auth.models
# Create your models here.


class Developer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}"

    class Meta:
        verbose_name = 'Разработчик'
        verbose_name_plural = 'Разработчики'
