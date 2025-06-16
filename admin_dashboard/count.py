from datetime import datetime, timedelta
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from admin_dashboard.models import visitor_count
from chatbot_app.models import profile_data


@csrf_exempt
def total_count(request):
    try:
        data = profile_data.objects.all().count()
        context = {
            'status': 'success',
            'data': data
        }
        return JsonResponse(context)
    except Exception as e:
        context = {
            'status': 'failed',
            'error': str(e)
        }
        return JsonResponse(context)


@csrf_exempt
def new_count(request):
    try:
        now = datetime.now()
        last_7_days = timedelta(days=7)
        count = now - last_7_days
        data = profile_data.objects.filter(created_at__gt=count).count()
        context = {
            'status': 'success',
            'data': data
        }
        return JsonResponse(context)
    except Exception as e:
        context = {
            'status': 'failed',
            'error': str(e)
        }
        return JsonResponse(context)


@csrf_exempt
def visitors(request):
    if request.method == 'POST':
        try:
            obj_count = visitor_count.objects.get()
            count = obj_count.v_count
            count_new = count + 1
            obj_count.v_count = count_new
            obj_count.save()
            context = {
                'status': 'success',
            }
            return JsonResponse(context)
        except Exception as e:
            context = {
                'status': 'failed',
                'error': str(e)
            }
            return JsonResponse(context)


@csrf_exempt
def get_visitors_count(request):
    try:
        total_count = visitor_count.objects.get()
        count = total_count.v_count
        context = {
            'status': 'success',
            'total_count': count
        }
        return JsonResponse(context)
    except Exception as e:
        context = {
            'status': 'failed',
            'error': str(e)
        }
        return JsonResponse(context)