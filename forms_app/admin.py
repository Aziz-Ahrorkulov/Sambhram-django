from django.contrib import admin

# Register your models here.
from .models import JobApplication

@admin.register(JobApplication)
class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name','gender', )