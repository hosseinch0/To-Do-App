from django.db import models
from django.contrib.auth.models import User
# from phonenumber_field.modelfields import PhoneNumberField


'''
A MODEL FOR OUR USER'S PROFILES 
'''


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    Image = models.ImageField(
        upload_to="media/profiles/", null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    isVip = models.BooleanField(null=True, default=False, blank=True)
    sex = models.CharField(max_length=50, null=True, blank=True)
    phoneNumber = models.CharField(max_length=255, null=True, blank=True)
    job = models.CharField(max_length=255, null=True, blank=True)
    educationField = models.CharField(max_length=255, null=True, blank=True)
    degree = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username

# python manage.py migrate --run-syncdb


class Address(models.Model):
    user = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    postalCode = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.user
