from django.urls import path
from admin_dashboard import views, count, timings, apply_doctor, mail

urlpatterns = [
    path('add_doctor/', views.add_doctor, name='add_doctor'),
    path('get_doctor/', views.get_doctor, name='get_doctor'),
    path('update_doctor/', views.update_doctor, name='update_doctor'),
    path('delete_doctor/<int:pk>/', views.delete_doctor, name='delete_doctor'),
    path('get_single_doctor/', views.get_single_doctor, name='get_single_doctor'),
    path('get_patients/', views.get_patients, name='get_patients'),
    path('total_count/', count.total_count, name='total_count'),
    path('new_count/', count.new_count, name='new_count'),
    path('visitors/', count.visitors, name='visitors'),
    path('get_visitors_count/', count.get_visitors_count, name='get_visitors_count'),
    path('add_timing/', timings.add_timing, name='add_timing'),
    path('get_timing/', timings.get_timings, name='get_timing'),
    path('apply/', apply_doctor.apply, name='apply'),
    path('get_applied_doctor_list/', apply_doctor.get_applied_doctor_list, name='get_applied_doctor_list'),
    path('doctor_verification/', apply_doctor.doctor_verification, name='doctor_verification'),
    path('get_approved_list/', apply_doctor.get_approved_list, name='get_approved_list'),
]

