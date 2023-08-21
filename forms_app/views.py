from django.shortcuts import render, redirect
from .forms import JobApplicationForm

# Create your views here.

def home(request):
    return render(request, 'index.html')


def thank_you(request):
    return render(request, 'thank_you.html')






def job_application(request):
    if request.method == 'POST':
        
        form = JobApplicationForm(request.POST, request.FILES)
        
        if form.is_valid():
            
            form.save()
            return redirect('thank_you')
    else:
        
        form = JobApplicationForm()
    return render(request, 'application.html', {'form': form})
