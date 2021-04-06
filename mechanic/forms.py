from django import forms

class DirectionForm(forms.Form):
    m_lat = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'m_lat'}))
    m_lon = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'m_lon'}))
    c_lat = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'c_lat'}))
    c_lon = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'c_lon'}))

class HelpsReceivedForm(forms.Form):
    customer_name = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'customer_name_HelpsReceivedForm'}))
    mechanic_name = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'mechanic_name_HelpsReceivedForm'}))
    email = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'email_HelpsReceivedForm'}))
    customer_email = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'customer_email_HelpsReceivedForm'}))
    contact_no = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'contact_no_HelpsReceivedForm'}))
    customer_contact_no = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'customer_contact_no_HelpsReceivedForm'}))
    customer_description = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'customer_description_HelpsReceivedForm'}))
    latitude = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'latitude_HelpsReceivedForm'}))
    longitude = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'longitude_HelpsReceivedForm'}))
    customer_latitude = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'customer_latitude_HelpsReceivedForm'}))
    customer_longitude = forms.CharField(label='', max_length=100, widget= forms.TextInput(attrs={'id':'customer_longitude_HelpsReceivedForm'}))
