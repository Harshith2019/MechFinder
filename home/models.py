from django.db import models
from django.contrib.auth.models import User
#from phonenumber_field.modelfields import PhoneNumberField
#from phone_field import PhoneField


class UserProfile(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, related_name='profile')
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20) #PhoneNumberField(null=False, blank=False, unique=True)
    #phone_number = PhoneField(blank=True, help_text='Contact phone number')
    #phone = PhoneNumberField()
    isMech = models.BooleanField(default=False)


    class Meta:
        ordering = ['-isMech',]

    def __str__(self):
        return self.firstname
