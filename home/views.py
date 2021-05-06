from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserProfileForm
from django.contrib.auth.models import User, AnonymousUser
from .models import UserProfile
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect


def home(request):
    if (request.user.is_authenticated):
        print(request.user)
        #return HttpResponseRedirect(reverse('customer', args=['you have already logged in']))
        #return customer(request, 'you have already logged in')
        return redirect('customer')
    else:
        print(request.user,'in else')
        return render(request, 'home/index.html')

def services(request):
    print(request.path)
    return render(request, 'home/services.html')

def about(request):
    return render(request, 'home/about.html')

def faqs(request):
    return render(request, 'home/faqs.html')

@login_required
def customer(request, error='error'):
    name = get_object_or_404(UserProfile, pk = request.user.id, user=request.user)
    userName = get_object_or_404(User, pk=request.user.id).username
    return render(request, 'home/customer.html', {'name':name, 'username':userName, 'error':error})


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'home/signupuser.html', {'form1':UserCreationForm(), 'form2':UserProfileForm()})
    else:
        mail = request.POST.get('email')
        try:
            existUser = UserProfile.objects.get(email=mail)
        except:
            existUser = None
        if existUser:
            return render(request, 'home/signupuser.html', {'form1':UserCreationForm(), 'form2':UserProfileForm(), 'error':'Account already exists with this email address!!'})
        else:
            if request.POST['password1'] == request.POST['password2']:
                print(request.POST.get('firstname'),request.POST.get('isMech'),' - wdh3r32')
                print('in else if',request.POST)
                password = request.POST.get('password1')
                if any(char.isdigit() for char in password) and any(char.isupper() for char in password) and any(not char.isalnum() for char in password) and len(password)>7:
                    try:
                        user = User.objects.create_user(username=request.POST.get('username'), password=request.POST['password1'])
                        user.save()
                        login(request, user)
                        form = UserProfileForm(request.POST)

                        if form.is_valid():
                            obj = form.save(commit=False)
                            obj.user = request.user
                            obj.save()
                        return redirect('customer')
                    except IntegrityError:
                        return render(request, 'home/signupuser.html', {'form1':UserCreationForm(), 'form2':UserProfileForm(), 'error':'Username already taken. Please try another username'})
                    except Exception as e:
                        return render(request, 'home/signupuser.html', {'form1':UserCreationForm(), 'form2':UserProfileForm(), 'error':'Something went wrong! Try Reloading'})
                else:
                    return render(request, 'home/signupuser.html', {'form1':UserCreationForm(), 'form2':UserProfileForm(), 'error':'Follow conditions to set password'})

            else:
                return render(request, 'home/signupuser.html', {'form1':UserCreationForm(), 'form2':UserProfileForm(), 'error':'Passwords didn\'t match'})


def loginuser(request):
    if (request.user.is_authenticated):
        print(request.user)
        return redirect('customer')

    if request.method == 'GET':
        return render(request, 'home/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'home/loginuser.html', {'form':AuthenticationForm(), 'error':'Entered wrong Username or password! Please try again!!'})
        else:
            login(request, user)
            return redirect('customer')

@login_required
def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return render(request, 'home/index.html')

@login_required
def editProfile(request):
    profile = get_object_or_404(UserProfile, pk=request.user.id, user=request.user)
    userName = get_object_or_404(User, pk=request.user.id).username

    if request.method == "GET":
        form = UserProfileForm(instance=profile)
        return render(request, 'home/profileDetails.html', {'form':form, 'username':userName})
    else:
        try:
            form = UserProfileForm(request.POST, instance=profile)
            form.save()
            return redirect('customer')
        except ValueError:
            #return render(request, 'todo/tododetail.html', {'form':TodoCreateForm(instance=form), 'error':'Bad input! Try again.'})
            return render(request, 'home/profileDetails.html', {'form':form, 'username':userName, 'error':'Bad input! Try again.'})
        except:
            #return render(request, 'todo/tododetail.html', {'form':TodoCreateForm(instance=form), 'error':'Bad input! Try again.'})
            return render(request, 'home/profileDetails.html', {'form':form, 'username':userName, 'error':'Something went wrong! Try again'})
