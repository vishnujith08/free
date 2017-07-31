from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

# Create your models here.
class User(AbstractUser):
    address = models.CharField(max_length=50,null=True,blank=True)
    mobile = models.IntegerField(default=1)
    image = models.ImageField(upload_to='user')


    objects = UserManager()

    def __str__(self):
        return self.first_name