from django import forms

class DirectionForm(forms.Form):
    m_lat = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'m_lat'}))
    m_lon = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'m_lon'}))
    c_lat = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'c_lat'}))
    c_lon = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'c_lon'}))
