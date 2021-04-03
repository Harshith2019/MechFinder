from .models import UserProfile
from django.forms import ModelForm
from django import forms
#from phonenumber_field.formfields import PhoneNumberField

#class ClientForm(forms.Form):
#    phone = PhoneNumberField()

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['firstname', 'lastname', 'email', 'phone', 'isMech']
        labels = {
            'firstname': "First Name",
            'lastname': "Last name",
            'email' : "Email id",
            'phone' : "Phone Number",
            'isMech' : "Are you a mechanic? "
        }

        widgets = {
            'firstname': forms.TextInput(attrs={'placeholder': 'First name'}),
            'lastname': forms.TextInput(attrs={'placeholder': 'Last name'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Ex: +91 abc-def-ghij'}),
            'email': forms.TextInput(attrs={'placeholder': 'Ex: xyz@example.com'}),
        }
