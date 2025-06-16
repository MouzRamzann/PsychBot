import os
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .forms import SignupForm
from django.contrib.auth import authenticate, logout, login
from django.core.files.storage import FileSystemStorage
from random import randint
from datetime import datetime, timedelta
from chatbot import settings
from django.core.mail import send_mail
import re
from .models import CustomUser


# Create your views here.
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def check_email(email):
    if re.search(regex, email):
        res = "Valid Email"
    else:
        res = "Invalid Email"
    return res


@csrf_exempt
def signup_request(request):
    if request.method == 'POST':
        try:
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                email = form.cleaned_data.get('email')
                user = authenticate(email=email, password=raw_password)
                if user is not None:
                    OTP = random_with_N_digits(4)
                    now = datetime.now()
                    now_plus_60_minutes = now + timedelta(minutes=60)
                    user.OTP_generated_datetime = now
                    user.OTP_expiration_datetime = now_plus_60_minutes
                    user.OTP = OTP
                    email_response = confirm_email(OTP, email)
                    user.save()
                    user_id = user.id
                    context = {
                        'status': 'success',
                        'user_id': user_id
                    }
                    # return render(request, 'authen/otp_verification.html', context)
                    return redirect('userOTPVerification')
                else:
                    error = form.errors
                    print(error)
                    if error == 'password2':
                        context = {
                            'status': 'failed',
                            'error': 'There is an issue with saving all info.',
                        }
                        return render(request, 'authen/signup.html', context)
            else:
                error = form.errors
                context = {
                    'status': 'failed',
                    'error': error,
                }
                return render(request, 'authen/signup.html', context)
        except Exception as e:
            context = {
                'status': 'failed',
                'error': str(e),
            }
            return render(request, 'authen/signup.html', context)
    return render(request, 'authen/signup.html')


@csrf_exempt
def login_request(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                error = 'Invalid username or password'
                context = {
                    'status': 'failed',
                    'error': error,
                }
                return render(request, 'authen/login.html', context)
        except Exception as e:
            error = 'Invalid username or password'
            context = {
                'status': 'failed',
                'error': error,
            }
            return render(request, 'authen/login.html', context)
    return render(request, 'authen/login.html')


def confirm_email(OTP, email_address):
    try:
        subject = 'Thank you for registering to our site'
        message = 'Here is your OTP to Get Registered on Psych-Bot '+'"'+str(OTP)+'"  .' 'This OTP can be used for ' \
                                                                                 'next 60 minutes.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email_address]
        send_mail(subject, message, email_from, recipient_list)
        return True
    except Exception as e:
        return str(e)


@csrf_exempt
def userOTPVerification(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        # email = 'tayyab@projectz.io'
        OTP = request.POST.get("OTP")
        try:
            obj_account_data_verified = CustomUser.objects.filter(email=email, is_account_verified=True).exists()
            if obj_account_data_verified:
                context = {
                    "status": "failed",
                    "description": "Your account is already verified.",
                    "Error": ''
                }
                return redirect('login')
                # return render(request, 'authen/otp_verification.html', context)
            else:
                obj_account_data_verified = CustomUser.objects.get(email=email)
                saved_OTP = obj_account_data_verified.OTP
                now = str(datetime.now().strftime('%Y%m%d%H%M%S.%f'))
                now_plus_60minutes = str(obj_account_data_verified.OTP_expiration_datetime.strftime('%Y%m%d%H%M%S.%f'))
                if now < now_plus_60minutes:
                    if OTP == saved_OTP:
                        obj_account_data_verified.is_account_verified = True
                        obj_account_data_verified.save()
                        context = {
                            "status": "ok",
                            "description": "Your account has been verified successfully.",
                            "Error": ''
                        }
                        return redirect('login')
                    else:
                        context = {
                            "status": "failed",
                            "description": "Your OTP is wrong and E-mail could not be verified.",
                            "Error": ''
                        }
                        return render(request, 'authen/otp_verification.html', context)
                else:
                    context = {
                        "status": "failed",
                        "description": "Your OTP has been expired and E-mail could not be verified.",
                        "Error": ''
                    }
                    # return redirect('login')
                    return render(request, 'authen/otp_verification.html', context)
        except Exception as e:
            context = {
                "status": "failed",
                "error": str(e)
            }
            return render(request, 'authen/otp_verification.html', context)
    return render(request, 'authen/otp_verification.html')


@csrf_exempt
def regenerate_OTP_API(request):
    if request.method == 'POST':
        user_id = request.POST.get("user_id")
        OTP = random_with_N_digits(4)
        try:
            user = CustomUser.objects.get(pk=user_id)
        except Exception as e:
            context = {
                "status": "failed",
                "description": "No user found.",
                "error": str(e)
            }
            return JsonResponse(context)
        email = user.email
        confirm_email(OTP, email)
        user.OTP = OTP
        now = datetime.now()
        now_plus_60minutes = now + timedelta(minutes=60)
        user.OTP_generated_datetime = now
        user.OTP_expiration_datetime = now_plus_60minutes
        user.save()
        context = {
            "status": "success",
            "description": "Your new OTP has been sent to your E-mail account.",
            "error": "NO error"
        }
        return JsonResponse(context)
    else:
        context = {
            "status": "failed",
            "description": "",
            "error": "Invalid request."
        }
        return JsonResponse(context)


@csrf_exempt
def userForgotPassword(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        try:
            user = CustomUser.objects.filter(email=username).exists()
            if user:
                user = CustomUser.objects.get(email=username)
                OTP = random_with_N_digits(4)
                email = user.email
                password_reset_email(OTP, email)
                user.password_reset_OTP = OTP
                now = datetime.now()
                now_plus_60minutes = now + timedelta(minutes=60)
                user.password_reset_request = True
                user.password_reset_request_sent_datetime = now
                user.password_reset_request_expiration = now_plus_60minutes
                user.save()
                return redirect('new_password_using_OTP')
        except Exception as e:
            context = {
                "status": "failed",
                "description": "No user found against this email / phone .",
                "error": str(e)
            }
            return render(request, 'authen/forget_password.html', context)
    else:
        return render(request, 'authen/forget_password.html')


def password_reset_email(OTP, email_address):
    try:
        subject = 'Thank you for registering to our site'
        message = 'Here is your OTP to change your password on Psych-Bot '+'"'+str(OTP)+'".' \
                                                                                       'This OTP can be used for next '\
                                                                                       '60 minutes. '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email_address]
        send_mail(subject, message, email_from, recipient_list)
        return True
    except Exception as e:
        return str(e)


@csrf_exempt
def new_password_using_OTP(request):
    if request.method == 'POST':
        OTP = request.POST.get('OTP')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        email = request.POST.get('email')
        if new_password == confirm_password:
            try:
                user = CustomUser.objects.filter(email=email).exists()
                if user:
                    user = CustomUser.objects.get(email=email)
                    saved_OTP = user.password_reset_OTP
                    now = str(datetime.now().strftime('%Y%m%d%H%M%S.%f'))
                    password_reset_request_expiration = str(
                        user.password_reset_request_expiration.strftime('%Y%m%d%H%M%S.%f'))
                    if now < password_reset_request_expiration:
                        if OTP == saved_OTP and user.password_reset_request:
                            user.set_password(new_password)
                            user.password_reset_request = False
                            user.save()
                            context = {
                                "status": "success",
                                "description": "your password has been changed successfully",
                                "Error": ''
                            }
                            return redirect('login')
                            # return JsonResponse(context)
                        else:
                            context = {
                                "status": "failed",
                                "description": "Your OTP is wrong and password could not be reset.",
                                "Error": ''
                            }
                            return render(request, 'authen/new_password.html', context)
                            # return JsonResponse(context)
                    else:
                        context = {
                            "status": "failed",
                            "description": "Your OTP has been expired and password could not be reset.",
                            "Error": ''
                        }
                        return render(request, 'authen/new_password.html', context)
                        # return JsonResponse(context)
            except Exception as e:
                context = {
                    "status": "failed",
                    "description": "No user found against this email / phone .",
                    "error": str(e)
                }
                # return JsonResponse(context)
                return render(request, 'authen/new_password.html', context)
    return render(request, 'authen/new_password.html')



def numOfDays(date1, date2):
    return (date2 - date1).days

@csrf_exempt
def user_forget_password_OTP_verification(request):
    OTP = request.POST.get('OTP')
    user_id = request.POST.get('user_id')
    try:
        user = CustomUser.objects.get(pk=user_id)
        if user:
            saved_OTP = user.password_reset_OTP
            now = str(datetime.now().strftime('%Y%m%d%H%M%S.%f'))
            password_reset_request_expiration = str(
                user.password_reset_request_expiration.strftime('%Y%m%d%H%M%S.%f'))
            if now < password_reset_request_expiration:
                if OTP == saved_OTP and user.password_reset_request:
                    context = {
                        "status": "success",
                        "description": "your OTP is verified",
                        "Error": ''
                    }
                    return JsonResponse(context)
                else:
                    context = {
                        "status": "failed",
                        "description": "Your OTP is wrong.",
                        "Error": ''
                    }
                    return JsonResponse(context)
            else:
                context = {
                    "status": "failed",
                    "description": "Your OTP has been expired",
                    "Error": ''
                }
                return JsonResponse(context)
    except Exception as e:
        context = {
            "status": "failed",
            "description": "No user found against this userID .",
            "error": str(e)
        }
        return JsonResponse(context)


def logout_req(request):
    logout(request)
    return redirect('login')
