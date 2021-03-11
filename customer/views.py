from django.shortcuts import render
from .forms import LocationModelForm
import folium

# Create your views here.

def index(request):

    form = LocationModelForm(request.POST or None)

    # initial values
    # l_lat = '33.8688'
    # l_lon = '151.2093'
    # m = folium.Map(width=800, height=500, location=[l_lat, l_lon], zoom_start=8)
    # folium.Marker([l_lat, l_lon], tooltip="click here for more", popup="Hey!",
    #                 icon=folium.Icon(color='purple')).add_to(m)

    m = None

    if form.is_valid():
        instance = form.save(commit=False)
        instance.latitude = form.cleaned_data.get('latitude')
        instance.longitude = form.cleaned_data.get('longitude')

        l_lat = instance.latitude
        l_lon = instance.longitude

        # initial folium map
        m = folium.Map(width=800, height=500, location=[l_lat, l_lon], zoom_start=8)

        # location Marker
        folium.Marker([l_lat, l_lon], tooltip="click here for more info", popup=[l_lat, l_lon],
                        icon=folium.Icon(color='purple')).add_to(m)

        m = m._repr_html_()

    if m:
        context = {
            'form': form,
            'map': m
        }
    else:
        context = {
            'form': form,
        }
    return render(request, 'customer/index.html', context)
