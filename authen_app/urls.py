from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('signup/', views.signup_request, name='signup'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_req, name='logout'),
    path('userOTPVerification/', views.userOTPVerification, name='userOTPVerification'),
    path('regenerate_OTP/', views.regenerate_OTP_API, name='regenerate_OTP_API'),
    path('userForgotPassword/', views.userForgotPassword, name='userForgotPassword'),
    path('new_password_using_OTP/', views.new_password_using_OTP, name='new_password_using_OTP'),
]