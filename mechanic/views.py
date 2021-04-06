from django.shortcuts import render, redirect, get_object_or_404
from .forms import DirectionForm, HelpsReceivedForm
from .utils import get_googlemaps_direction_url
from django.contrib.auth.models import User

from home.models import UserProfile
from customer.models import helps_received
from .models import need_help

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):

    try:
        pending_requests = helps_received.objects.get(mechanic_name=get_object_or_404(User, pk=request.user.id).username)
        return redirect('pending_order/')
        print('------>   Having pending orders!')
    except:
        pending_requests = None
        print('------>   No pending orders!')

    direction_form = DirectionForm(request.POST or None)

    if request.method == 'POST' and not direction_form.is_valid():
        print(request.POST)
        helps_received_instance = helps_received()
        helps_received_instance.customer_name = request.POST['customer_name']
        helps_received_instance.mechanic_name = request.POST['mechanic_name']
        helps_received_instance.email = request.POST['email']
        helps_received_instance.customer_email = request.POST['customer_email']
        helps_received_instance.contact_no = request.POST['contact_no']
        helps_received_instance.customer_contact_no = request.POST['customer_contact_no']
        helps_received_instance.latitude = request.POST['latitude']
        helps_received_instance.longitude = request.POST['longitude']
        helps_received_instance.customer_latitude = request.POST['customer_latitude']
        helps_received_instance.customer_longitude = request.POST['customer_longitude']
        helps_received_instance.save()

        # incase the customer was able to give more than one request, delete remaing too
        request_obj_count = need_help.objects.filter(user_name=request.POST['customer_name']).count()
        if request_obj_count > 0:
            for i in range(0, request_obj_count):
                request_obj =  need_help.objects.filter(user_name=request.POST['customer_name']).first()
                request_obj.delete()

        return redirect('pending_order/')


    name = get_object_or_404(UserProfile, pk = request.user.id, user=request.user)
    email = get_object_or_404(UserProfile, pk = request.user.id, user=request.user).email
    phone = get_object_or_404(UserProfile, pk = request.user.id, user=request.user).phone
    userName = get_object_or_404(User, pk=request.user.id).username

    direction_form = DirectionForm(request.POST or None)
    help_form = HelpsReceivedForm(request.POST or None)
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
        'name': name,
        'userName': userName,
        'email': email,
        'phone': phone,
        'direction_form': direction_form,
        'maps_url': maps_url,
        'help_form': help_form,
    }

    return render(request, 'mechanic/index.html', context)

@login_required
def pending_order(request):

    try:
        pending_requests = helps_received.objects.get(mechanic_name=get_object_or_404(User, pk=request.user.id).username)
    except:
        pending_requests = None

    context = {
        'pending_requests': pending_requests
    }

    return render(request, 'mechanic/pending_order.html', context)
