
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserCreateForm
from django.contrib.auth.models import User
from .models import UserCreateModel
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
#from .forms import TodoCreateForm
#from .models import TodoModel
from django.utils import timezone
from django.contrib.auth.decorators import login_required




def home(request):
    return render(request, 'MechFinder/home.html')


def loginuser(request):
    return render(request, 'MechFinder/loginuser.html')



def signupuser(request):
    if request.method == 'GET':
        return render(request, 'MechFinder/signupuser.html', {'form':UserCreateForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = UserCreateModel.objects.create_user(username=request.POST.get('username'), password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'MechFinder/signupuser.html', {'form':UserCreateForm(), 'error':'Username already taken. Please try another username'})
        else:
            return render(request, 'MechFinder/signupuser.html', {'form':UserCreateForm(), 'error':'Passwords didn\'t match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'MechFinder/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'MechFinder/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password doesn\'t exist'})
        else:
            login(request, user)
            return redirect('home')
