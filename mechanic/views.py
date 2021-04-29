from django.shortcuts import render
from .forms import DirectionForm
from .utils import get_googlemaps_direction_url

# Create your views here.

def index(request):

    direction_form = DirectionForm(request.POST or None)
    maps_url = None

    if direction_form.is_valid():
        m_lat = float(direction_form.cleaned_data.get('m_lat'))
        m_lon = float(direction_form.cleaned_data.get('m_lon'))
        c_lat = float(direction_form.cleaned_data.get('c_lat'))
        c_lon = float(direction_form.cleaned_data.get('c_lon'))
        maps_url = str(get_googlemaps_direction_url(m_lat, m_lon, c_lat, c_lon))
        print(m_lat)
        print(m_lon)
        print(c_lat)
        print(c_lon)
        print(maps_url)


    context = {
        'direction_form': direction_form,
        'maps_url': maps_url,
    }

    return render(request, 'mechanic/index.html', context)
