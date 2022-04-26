from django.db import models
from datetime import datetime


class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name