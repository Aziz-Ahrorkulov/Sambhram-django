from django.urls import path
from . import views

urlpatterns = [
    path('user-admin/', views.view_applications, name='dashboard-index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout-user/', views.logout_user, name='logout'),

]