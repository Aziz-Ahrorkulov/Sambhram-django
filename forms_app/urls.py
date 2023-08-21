from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),   
    path('job_application/', views.job_application, name='job_application'),
    path('thank_you/', views.thank_you, name='thank_you'),
]