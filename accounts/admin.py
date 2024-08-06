from django.contrib.admin import AdminSite
from django.contrib import admin
from .models import UserProfile

class CustomAdminSite(AdminSite):
    site_header = 'WIKITUBE ADMIN'
    site_title = 'WIKITUBE'
    index_title = 'Welcome to WIKITUBE'

custom_admin_site = CustomAdminSite(name='custom_admin')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'phone_number', 'first_name', 'last_name', 'email', 'is_admin', 'is_staff', 'is_active', 'is_superadmin')  # Updated fields

custom_admin_site.register(UserProfile, UserProfileAdmin)
