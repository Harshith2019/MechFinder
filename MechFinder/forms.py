from .models import UserCreateModel
from django import forms


class UserCreateForm(forms.ModelForm):
    #password1 = forms.CharField(widget=forms.PasswordInput)
    #password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = UserCreateModel
        #fields = ['username', 'password1', 'password2', 'mech_or_cust']
        #fields = ['user', 'mech_or_cust']
        #exclude = []
        fields = '__all__'
