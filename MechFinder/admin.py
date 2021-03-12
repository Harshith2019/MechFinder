from django.contrib import admin
from .models import UserCreateModel


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import UserCreateModel

'''
# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class UserCreateModelInline(admin.StackedInline):
    model = UserCreateModel
    can_delete = False
    verbose_name_plural = 'UserCreateModel'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserCreateModelInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
'''

admin.site.register(UserCreateModel, BaseUserAdmin)
