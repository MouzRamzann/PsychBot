from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from admin_dashboard.models import doctor
from chatbot_app.models import profile_data
from chatbot_app.views import BASE_DIR


# Create your views here.

@login_required(login_url='login')
@csrf_exempt
def add_doctor(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            country = request.POST.get('country')
            number = request.POST.get('number')
            qualification = request.POST.get('qualification')
            image = request.FILES.get('image')
            workspace = request.POST.get('workspace')
            email = request.POST.get('email')

            fs = FileSystemStorage()
            image_save = fs.save(f'{BASE_DIR}/static/doc_profile/' + image.name, image)
            image_url = fs.url(image_save)

            obj_doctor = doctor()
            obj_doctor.name = name
            obj_doctor.country = country
            obj_doctor.number = number
            obj_doctor.image = image_url
            obj_doctor.qualification = qualification
            obj_doctor.workspace = workspace
            obj_doctor.email = email
            obj_doctor.save()
            context = {
                'status': 'success'
            }
            return JsonResponse(context)
        except Exception as e:
            context = {
                'status': 'failed',
                'error': str(e)
            }
            return JsonResponse(context)
    return render(request, 'dashboard/doctor_list.html')


@login_required(login_url='login')
@csrf_exempt
def get_doctor(request):
    if request.method == 'POST':
        try:
            country = request.POST.get('country')
            details = doctor.objects.filter(country=country)
            doctor_list = []
            for i in details:
                doctor_list.append({'pk': i.pk,
                                    'name': i.name,
                                    'country': i.country,
                                    'qualification': i.qualification,
                                    'email': i.email,
                                    'number': i.number,
                                    'image': i.image,
                                    'workspace': i.workspace})
            context = {
                'doctor_list': doctor_list
            }
            return JsonResponse(context)
        except Exception as e:
            context = {
                'status': 'failed',
                'error': str(e)
            }
            return JsonResponse(context)
    return render(request, 'dashboard/doctor_list.html')


@csrf_exempt
def get_single_doctor(request):
    if request.method == 'POST':
        try:
            pk = request.POST.get('pk')
            doctor_data = []
            details = doctor.objects.filter(pk=pk)
            for i in details:
                doctor_data.append({'pk': i.pk,
                                    'name': i.name,
                                    'country': i.country,
                                    'qualification': i.qualification,
                                    'email': i.email,
                                    'number': i.number,
                                    'image': i.image,
                                    'workspace': i.workspace})
            context = {
                'status': 'success',
                'doctor_data': doctor_data,
            }
            return JsonResponse(context)
        except Exception as e:
            context = {
                'status': 'failed',
                'error': str(e)
            }
            return JsonResponse(context)


@login_required(login_url='login')
@csrf_exempt
def update_doctor(request):
    if request.method == 'POST':
        try:
            pk = request.POST.get('pk')
            name = request.POST.get('name')
            country = request.POST.get('country')
            number = request.POST.get('number')
            qualification = request.POST.get('qualification')
            workspace = request.POST.get('workspace')
            email = request.POST.get('email')

            obj_doctor = doctor.objects.get(pk=pk)
            obj_doctor.name = name
            obj_doctor.country = country
            obj_doctor.number = number
            obj_doctor.qualification = qualification
            obj_doctor.workspace = workspace
            obj_doctor.email = email
            obj_doctor.save()
            context = {
                'status': 'success'
            }
            return JsonResponse(context)
        except Exception as e:
            context = {
                'status': 'failed',
                'error': str(e)
            }
            return JsonResponse(context)
    return render(request, 'dashboard/doctor_list.html')


@login_required(login_url='login')
@csrf_exempt
def delete_doctor(request, pk):
        try:
            obj_doctor = doctor.objects.get(pk=pk)
            obj_doctor.delete()

            context = {
                'status': 'success'
            }
            return redirect('get_doctor')
            # return JsonResponse(context)
        except Exception as e:
            context = {
                'status': 'failed',
                'error': str(e)
            }
            return redirect('get_doctor')


@login_required(login_url='login')
@csrf_exempt
def get_patients(request):
    if request.method == 'POST':
        try:
            country = request.POST.get('country')
            data = profile_data.objects.filter(country=country)
            patient_list = []
            for i in data:
                patient_list.append({'first_name': i.f_name,
                                     'address': i.address,
                                     'education': i.education,
                                     'marital_status': i.marital_status,
                                     'profession': i.profession,
                                     'age': i.age,
                                     })
            context = {
                'status': 'success',
                'patient_list': patient_list
            }
            return JsonResponse(context)
        except Exception as e:
            context = {
                'status': 'failed',
                'error': str(e)
            }
            return JsonResponse(context)
    return render(request, 'dashboard/admin_dashboard.html')
