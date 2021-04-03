from django.db import models

# Create your models here.

class need_help(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    contact_no = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def get_all_objects(self):
        queryset = self._meta.model.objects.all().values('name', 'email', 'description', 'contact_no')
        # can use the below method also
        # queryset = self.__class__.objects.all()
        return list(queryset)
