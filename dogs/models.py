from django.db import models
from django.utils import timezone
from django import forms
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class ServicePost(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    servicio = models.CharField(max_length=20)
    descripcion = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.namedog
