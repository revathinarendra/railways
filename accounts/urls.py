from django.urls import path
from . import views

urlpatterns = [
    # User registration and verification
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('verify-email/<uuid:token>/', views.verify_email, name='verify-email'),

    # User management
    path('current-user/', views.currentUser, name='current-user'),
    path('update-user/', views.updateUser, name='update-user'),

    # Password reset
    path('password-reset-request/', views.password_reset_request, name='password-reset-request'),
    path('password-reset-confirm/<uidb64>/<token>/', views.password_reset_confirm, name='password-reset-confirm'),
]
