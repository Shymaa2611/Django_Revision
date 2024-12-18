from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView,LogoutView

urlpatterns = [
    path('',Signup.as_view() ,name='signup'),
    path('login/', LoginView.as_view(template_name='pages/login.html'), name='login'),
    path('password-reset/', PasswordResetView.as_view(template_name='pages/password_reset.html'), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='pages/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='pages/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='pages/password_reset_complete.html'), name='password_reset_complete'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

