from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class UserCreateModel(AbstractUser):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    #username = models.CharField('Username:', max_length=50, primary_key = True)
    #password1 = models.CharField('Enter password:', max_length=20)
    #password2 = models.CharField('Confirm password:', max_length=20)
    email = models.CharField('Username:', max_length=50, unique = True)
    mech_or_cust = models.BooleanField(default=False)
    #datecreated = models.DateTimeField(auto_now_add=True)
    #last_login = models.DateTimeField(null=True, blank=True)

    #USERNAME_FIELD = 'email'
    #exclude = ['email']
    #REQUIRED_FIELDS = ['username', 'password1', 'password2', 'mech_or_cust']
    #REQUIRED_FIELDS = ['user', 'mech_or_cust']

    class Meta:
        ordering = ['mech_or_cust',]

    #def __str__(self):
    #    return self.user.username

'''
    USERNAME_FIELD = 'username'
    is_anonymous = False
    is_authenticated = True
'''
