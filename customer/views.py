from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from home.models import UserProfile
from mechanic.models import need_help
from .models import Location

from django.contrib.auth.decorators import login_required
from .forms import LocationModelForm, AskHelpForm
import folium

# Create your views here.

@login_required
def index(request):

    if request.method == 'POST':
        need_help_instance = need_help()
        need_help_instance.name = request.POST['name']
        need_help_instance.user_name = request.POST['user_name']
        need_help_instance.email = request.POST['email']
        need_help_instance.description = request.POST['description']
        need_help_instance.contact_no = request.POST['contact_no']
        need_help_instance.latitude = request.POST['latitude']
        need_help_instance.longitude = request.POST['longitude']
        need_help_instance.save()

    print("----->   ", request.user)
    print("----->   ", request.user.id)


    name = get_object_or_404(UserProfile, pk = request.user.id, user=request.user)
    email = get_object_or_404(UserProfile, pk = request.user.id, user=request.user).email
    phone = get_object_or_404(UserProfile, pk = request.user.id, user=request.user).phone
    userName = get_object_or_404(User, pk=request.user.id).username
    form = LocationModelForm(request.POST or None)
    ask_help_form = AskHelpForm(request.POST or None)


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
            'name': name,
            'userName': userName,
            'email': email,
            'phone': phone,
            'form': form,
            'ask_help_form': ask_help_form,
            'map': m,
            'display_lat_lon_form': 'none',
        }
    else:
        context = {
            'name': name,
            'userName': userName,
            'email': email,
            'phone': phone,
            'form': form,
            'ask_help_form': ask_help_form,
            'display_lat_lon_form': 'block',
        }
    return render(request, 'customer/index.html', context)
