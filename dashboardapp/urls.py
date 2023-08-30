from django.urls import path
from . import views

urlpatterns = [
    path('user-admin/', views.view_applications, name='dashboard-index'),
    path('workers/', views.workers, name='dashboard-workers'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout-user/', views.logout_user, name='logout'),
    path('download_resume/<int:application_id>/', views.download_resume, name='download_resume'),

]