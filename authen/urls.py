from django.contrib import admin
from django.urls import path, include, re_path

from authen import views
from django.contrib.auth import views as auth_views



# from django.conf.urls import url



urlpatterns = [
    # path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('otp_verification/', views.otp_verification, name='otp_verification'),
    path('forget_password/', views.forget_password, name='forget_password'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('not_found/', views.not_found, name='not_found'),
    path('', include('django.contrib.auth.urls')),

]