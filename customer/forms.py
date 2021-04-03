from django import forms
from .models import Location

class LocationModelForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('latitude', 'longitude')
        widgets = {
            'latitude': forms.TextInput(attrs={'id': 'latitude_id'}),
            'longitude': forms.TextInput(attrs={'id': 'longitude_id'}),
        }
        labels = {
            'latitude': "",
            'longitude': "",
        }

class AskHelpForm(forms.Form):
    name = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'name_AskHelpForm'}))
    email = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'email_AskHelpForm'}))
    description = forms.CharField(label='', max_length=1000, widget= forms.Textarea(attrs={'id':'description_AskHelpForm'}))
    contact_no = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'contact_no_AskHelpForm'}))
