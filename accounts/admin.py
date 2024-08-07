from django.contrib.admin import AdminSite
from django.contrib import admin
from .models import UserProfile

class CustomAdminSite(AdminSite):
    site_header = 'RAILWAY ADMIN'
    site_title = 'RAILWAY'
    index_title = 'Welcome to RAILWAY'

custom_admin_site = CustomAdminSite(name='custom_admin')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'phone_number', 'first_name', 'last_name', 'email', 'gender', 'is_admin', 'is_staff', 'is_active', 'is_superadmin')
    fields = ('user', 'date_of_birth', 'phone_number', 'first_name', 'last_name', 'email', 'gender', 'is_admin', 'is_staff', 'is_active', 'is_superadmin')
    # Optional: Define fieldsets if you want to group fields in the form
    # fieldsets = (
    #     (None, {
    #         'fields': ('user', 'date_of_birth', 'phone_number', 'first_name', 'last_name', 'email', 'gender')
    #     }),
    #     ('Permissions', {
    #         'classes': ('collapse',),
    #         'fields': ('is_admin', 'is_staff', 'is_active', 'is_superadmin'),
    #     }),
    # )

custom_admin_site.register(UserProfile, UserProfileAdmin)
