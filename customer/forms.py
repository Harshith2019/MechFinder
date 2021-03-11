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
