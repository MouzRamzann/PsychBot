from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm
from authen.forms import SignUpForm


# Create your views here.

@csrf_exempt
def signup(request):
    if request.user.is_superuser:
        return redirect(reverse("admin_dashboard"))
    if request.user.is_authenticated:
        return redirect(reverse("dashboard"))
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                # login(request, user)
                return redirect('login')
        else:
            error = form.errors
            print(error)
            if error == 'password2':
                print("The two password fields didn’t match.")
            form = SignUpForm()
            context = {
                'error': error,
                'form': form
            }
            return render(request, 'authen/signup.html', context)
    else:
        form = SignUpForm()
    return render(request, 'authen/signup.html', {'form': form})


@csrf_exempt
def login_request(request):
    redirect_to = request.GET.get('next', '/')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                error = 'Invalid username or password'
                return render(request, 'authen/login.html',{'error':error})
        else:
            error = 'Invalid username or password'
            return render(request, 'authen/login.html', {'error': error})
    else:
        if request.user.is_authenticated:
            return redirect(reverse("dashboard"))
        return render(request, 'authen/login.html', locals())


def logout_request(request):
    logout(request)
    return redirect('login')


def otp_verification(request):
    return render(request, 'authen/otp_verification.html')

def forget_password(request):
    return render(request, 'authen/forget_password.html')

def reset_password(request):
    return render(request, 'authen/new_password.html')

def not_found(request):
    return render(request, '404.html')