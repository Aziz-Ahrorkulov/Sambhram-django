from django.contrib import admin

# Register your models here.
from .models import JobApplication, Job

@admin.register(JobApplication)
class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name','gender', )

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    prepopulated_fields = {"slug" : ("title",)}