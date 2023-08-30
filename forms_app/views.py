from django.shortcuts import render, redirect
from .forms import JobApplicationForm
from .models import Job
# Create your views here.

def home(request):
    return render(request, 'index.html')


def thank_you(request):
    return render(request, 'thank_you.html')



def page_not_found(request, exception):
    return render(request, 'dashboard-templates/404.html', status=404)


def job_application(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = JobApplicationForm()
    context = {
        'form': form,
    }
    
    return render(request, 'application.html', context)
