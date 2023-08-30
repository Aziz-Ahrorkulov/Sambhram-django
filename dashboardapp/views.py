from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import AdminProfile, Workers
from forms_app.models import JobApplication, Job
from django.contrib.auth import logout,  authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import FileResponse
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

        
        
        # Перенаправляем на страницу с заявками
        
    
    admin_profile = AdminProfile.objects.filter(user=request.user).first()

    if admin_profile:
        applications = JobApplication.objects.filter(approval_status='pending', current_admin_stage=admin_profile.role)
    else:
        applications = JobApplication.objects.none()
        
    if request.method == 'POST':
        application_id = request.POST.get('application_id')
        action = request.POST.get('action')
        
        if action == 'approve':
            application = JobApplication.objects.get(id=application_id)
        
            # Получаем профиль администратора, который делает заявку
            admin_profile = AdminProfile.objects.get(user=request.user)

            # Проверяем, что администратор на этапе одобрения заявки
            if admin_profile.role == application.current_admin_stage :
                # Увеличиваем этап заявки
                application.current_admin_stage  += 1
                application.save()
            return redirect('dashboard-index')
    
        elif action == 'reject':
            application = JobApplication.objects.get(id=application_id)
            # Отклонить заявку
            application.approval_status = 'rejected'
            application.save()
        
        return redirect('dashboard-index')
    return render(request, 'dashboard-templates/dashboard-index.html', {'applications': applications, 'admin_profile': admin_profile})



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        last_name = request.POST['last_name']
        email = request.POST['email']
        admin_role = request.POST.get('admin_role') 
        password = request.POST['password']
        confirm_password = request.POST['password2']


        if User.objects.filter(username=username).exists():
            messages.error(request, 'This username is already taken.')
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

                    admin_profile = AdminProfile.objects.create(user=user, role=admin_role)
                    admin_profile.save()

                    response.set_cookie('cookies.authorization', str(user.id))
                    user.save()
                    return response
    else:
        return render(request, 'dashboard-templates/register.html')


def workers(request):
    jobs = Job.objects.all()
    workers = Workers.objects.all()

    active_category = request.GET.get('job', '')
    admin_profile = AdminProfile.objects.filter(user=request.user).first()

    if active_category:
        workers = workers.filter(job__slug=active_category)

    context = {
        'jobs' : jobs,
        'workers' : workers ,
        'active_category' : active_category,
        'admin_profile' : admin_profile
    }

    return render(request, 'dashboard-templates/workers.html', context)

def logout_user(request):
    logout(request)
    return redirect('home')

def download_resume(request, application_id):
    application = JobApplication.objects.get(id=application_id)
    response = FileResponse(application.resume)
    response['Content-Disposition'] = f'attachment; filename="{application.resume.name}"'
    return response

def page_not_found(request, exception):
    return render(request, 'dashboard-templates/404.html', status=404)