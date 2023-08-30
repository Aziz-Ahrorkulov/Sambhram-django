from django.contrib import admin
from .models import AdminProfile, Workers
from django.contrib.auth.models import Group, User

# Register your models here.

class ProfileInline(admin.StackedInline):
    model = AdminProfile

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username", 'first_name', 'last_name', 'password',]
    inlines = [ProfileInline]
    list_display = ('id', 'username', 'password')

admin.site.unregister(User)

# Register User
admin.site.register(User, UserAdmin)

admin.site.unregister(Group)

@admin.register(Workers)
class WorkersAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name')