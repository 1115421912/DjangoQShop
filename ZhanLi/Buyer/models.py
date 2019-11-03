from django.db import models

class User(models.Model):

    email = models.EmailField()
    password = models.CharField(max_length=18)
    username = models.CharField(max_length=32)
    age = models.CharField(max_length=4, null=True, blank=True)
    gender = models.CharField(max_length=4, null=True, blank=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    address = models.CharField(max_length=128, null=True, blank=True)
    picture = models.ImageField(upload_to='img', null=True, blank=True)

    user_type = models.CharField(max_length=4, null=True, blank=True)

# Create your models here.
