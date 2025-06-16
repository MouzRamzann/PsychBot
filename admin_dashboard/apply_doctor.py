from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from admin_dashboard.mail import send_email
from admin_dashboard.models import apply_as_doctor


@csrf_exempt
def apply(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            qualification = request.POST.get('qualification')
            number = request.POST.get('number')
            email = request.POST.get('email')
            city = request.POST.get('city')
            country = request.POST.get('country')

            obj_apply = apply_as_doctor()
            obj_apply.name = name
            obj_apply.qualification = qualification
            obj_apply.city = city
            obj_apply.email = email
            obj_apply.number = number
            obj_apply.country = country
            obj_apply.save()

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


@login_required(login_url='login')
@csrf_exempt
def get_applied_doctor_list(request):
    if request.method == 'POST':
        try:
            status = 0
            details = apply_as_doctor.objects.filter(status=status)
            list = []
            for i in details:
                list.append({'pk': i.pk,
                             'name': i.name,
                             'qualification': i.qualification,
                             'city': i.city,
                             'country': i.country,
                             'number': i.number,
                             'email': i.email})
            context = {
                'status': 'success',
                'list': list
            }
            return JsonResponse(context)
        except Exception as e:
            context = {
                'status': 'failed',
                'error': str(e)
            }
            return JsonResponse(context)
    return render(request, 'dashboard/applied_list.html')


# @login_required(login_url='login')
@csrf_exempt
def doctor_verification(request):
    if request.method == 'POST':
        try:
            pk = request.POST.get('pk')
            email = request.POST.get('email')
            value = request.POST.get('value')

            details = apply_as_doctor.objects.get(pk=pk)
            if value == 'approved':
                response = send_email(email, value)
                status = True

                details.status = status
                details.save()

                context = {
                    'status': 'success',
                    'response': response
                }
                return JsonResponse(context)
            else:
                response = send_email(email, value)
                data = apply_as_doctor.objects.get(pk=pk)
                data.delete()
                context = {
                    'status': 'success',
                    'response': response
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
def get_approved_list(request):
    if request.method == 'POST':
        try:
            status = 1
            data = apply_as_doctor.objects.filter(status=status)
            approved_doctors = []
            for i in data:
                approved_doctors.append({'name': i.name,
                                         'qualification': i.qualification,
                                         'city': i.city,
                                         'country': i.country,
                                         'number': i.number,
                                         'email': i.email})
            context = {
                'status': 'success',
                'approved_doctors': approved_doctors
            }
            return JsonResponse(context)
        except Exception as e:
            context = {
                'status': 'failed',
                'error': str(e)
            }
            return JsonResponse(context)
    return render(request, 'dashboard/approved_list.html')
