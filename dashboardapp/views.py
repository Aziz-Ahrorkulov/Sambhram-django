from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import AdminProfile
from forms_app.models import JobApplication
from django.contrib.auth import logout,  authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        
        if user != None:
            auth_login(request, user)
            response = redirect('dashboard-index')   
            response.set_cookie('cookies.authorization', str(user.id))
            return response

        else:

            messages.error(request, 'Username or password is not correct')
            response = render(request, 'dashboard-templates/login.html')        
            return response

    else:
        return render(request, 'dashboard-templates/login.html')

@login_required(login_url='login')
def view_applications(request):
    try:
        admin_profile = AdminProfile.objects.get(user=request.user)
    except AdminProfile.DoesNotExist:
        admin_profile = None

    if admin_profile and admin_profile.role == 2:
        applications = JobApplication.objects.all()
    else:
        applications = JobApplication.objects.none()

    return render(request, 'dashboard-templates/dashboard-index.html', {'applications': applications, 'admin_profile': admin_profile})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['password2']
        for usernames in User.objects.all():
                if usernames.username == username:
                    return redirect('register')
                else:
                    if password == confirm_password:
                        if username == "" or len(username) < 2 or last_name == "": 
                            messages.error(request, 'Usename too short')
                            return redirect('register')
                        elif 8 > len(password):
                            messages.error(request, 'This password is too short. It must contain at least 8 characters.')
                            return redirect('register')
                        else:
                            user = User.objects.create_user(username=username, email=email, last_name=last_name, password=password) 
                            auth_login(request, user)
                            response = redirect('home') 
                            response.set_cookie('cookies.authorization', str(user.id))
                            user.save()
                            return response
    else:
        return render(request, 'dashboard-templates/register.html')


def logout_user(request):
    logout(request)
    return redirect('home')