from django.db import models

# Create your models here.

class Location(models.Model):
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.latitude},{self.longitude}"
