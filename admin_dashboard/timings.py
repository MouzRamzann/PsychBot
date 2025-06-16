from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from admin_dashboard.models import doctor
from chatbot_app.models import doc_timing, timing_exists
from datetime import datetime, timedelta


@login_required(login_url='login')
@csrf_exempt
def add_timing(request):
    if request.method == 'POST':
        current_date = datetime.today()
        current_day = current_date.strftime('%A')  # Use strftime function
        print(current_day)
        try:
            pk = request.POST.get('pk')
            # monday = request.POST.get('monday')
            # tuesday = request.POST.get('tuesday')
            # wednesday = request.POST.get('wednesday')
            # thursday = request.POST.get('thursday')
            # friday = request.POST.get('friday')
            # saturday = request.POST.get('saturday')
            # sunday = request.POST.get('sunday')
            time1_mon = request.POST.get('time1_mon')
            # if time1_mon == '':
            #     time1_mon = None
            time2_mon = request.POST.get('time2_mon')
            # if time2_mon == '':
            #     time2_mon = None
            time3_mon = request.POST.get('time3_mon')
            # if time3_mon == '':
            #     time3_mon = None
            time1_tue = request.POST.get('time1_tue')
            # if time1_tue == '':
            #     time1_tue = None
            time2_tue = request.POST.get('time2_tue')
            # if time2_tue == '':
            #     time2_tue = None
            time3_tue = request.POST.get('time3_tue')
            # if time3_tue == '':
            #     time3_tue = None
            time1_wed = request.POST.get('time1_wed')
            # if time1_wed == '':
            #     time1_wed = None
            time2_wed = request.POST.get('time2_wed')
            # if time2_wed == '':
            #     time2_wed = None
            time3_wed = request.POST.get('time3_wed')
            # if time3_wed == '':
            #     time3_wed = None
            time1_thur = request.POST.get('time1_thur')
            # if time1_thur == '':
            #     time1_thur = None
            time2_thur = request.POST.get('time2_thur')
            # if time2_thur == '':
            #     time2_thur = None
            time3_thur = request.POST.get('time3_thur')
            # if time3_thur == '':
            #     time3_thur = None
            time1_fri = request.POST.get('time1_fri')
            # if time1_fri == '':
            #     time1_fri = None
            time2_fri = request.POST.get('time2_fri')
            # if time2_fri == '':
            #     time2_fri = None
            time3_fri = request.POST.get('time3_fri')
            # if time3_fri == '':
            #     time3_fri = None
            time1_sat = request.POST.get('time1_sat')
            # if time1_sat == '':
            #     time1_sat = None
            time2_sat = request.POST.get('time2_sat')
            # if time2_sat == '':
            #     time2_sat = None
            time3_sat = request.POST.get('time3_sat')
            # if time3_sat == '':
            #     time3_sat = None
            time1_sun = request.POST.get('time1_sun')
            # if time1_sun == '':
            #     time1_sun = None
            time2_sun = request.POST.get('time2_sun')
            # if time2_sun == '':
            #     time2_sun = None
            time3_sun = request.POST.get('time3_sun')
            # if time3_sun == '':
            #     time3_sun = None

            data = doctor.objects.get(pk=pk)

            # if monday == 'Monday':
            data.first_time_mon = time1_mon
            data.second_time_mon = time2_mon
            data.third_time_mon = time3_mon
                # data.save()
            # if tuesday == 'Tuesday':
            data.first_time_tue = time1_tue
            data.second_time_tue = time2_tue
            data.third_time_tue = time3_tue
                # data.save()
            # if wednesday == 'Wednesday':
            data.first_time_wed = time1_wed
            data.second_time_wed = time2_wed
            data.third_time_wed = time3_wed
                # data.save()
            # if thursday == 'Thursday':
            data.first_time_thur = time1_thur
            data.second_time_thur = time2_thur
            data.third_time_thur = time3_thur
                # data.save()
            # if friday == 'Friday':
            data.first_time_fri = time1_fri
            data.second_time_fri = time2_fri
            data.third_time_fri = time3_fri
                # data.save()
            # if saturday == 'Saturday':
            data.first_time_sat = time1_sat
            data.second_time_sat = time2_sat
            data.third_time_sat = time3_sat
                # data.save()
            # if sunday == 'Sunday':
            data.first_time_sun = time1_sun
            data.second_time_sun = time2_sun
            data.third_time_sun = time3_sun
            data.save()
            monday_time_list = [time1_mon, time2_mon, time3_mon]
            tuesday_time_list = [time1_tue, time2_tue, time3_tue]
            wednesday_time_list = [time1_wed, time2_wed, time3_wed]
            thursday_time_list = [time1_thur, time2_thur, time3_thur]
            friday_time_list = [time1_fri, time2_fri, time3_fri]
            saturday_time_list = [time1_sat, time2_sat, time3_sat]
            sunday_time_list = [time1_sun, time2_sun, time3_sun]
            row_exists = timing_exists.objects.filter(doctor_id=pk).exists()
            if row_exists:
                context = {
                    'error': 'Doctor_id already exists.'
                }
                return JsonResponse(context)
            else:
                if current_day == 'Monday':
                    for i in monday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day, timing=i, date=current_date)
                        doc_time.save()
                elif current_day == 'Tuesday':
                    for i in tuesday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day, timing=i, date=current_date)
                        doc_time.save()
                elif current_day == 'Wednesday':
                    for i in wednesday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day, timing=i, date=current_date)
                        doc_time.save()
                elif current_day == 'Thursday':
                    for i in thursday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day, timing=i, date=current_date)
                        doc_time.save()
                elif current_day == 'Friday':
                    for i in friday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day, timing=i, date=current_date)
                        doc_time.save()
                elif current_day == 'Saturday':
                    for i in saturday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day, timing=i, date=current_date)
                        doc_time.save()
                elif current_day == 'Sunday':
                    for i in sunday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day, timing=i, date=current_date)
                        doc_time.save()
                current_date_plus_one = datetime.today() + timedelta(days=1)
                current_day_plus_one = current_date_plus_one.strftime('%A')
                if current_day_plus_one == 'Monday':
                    for i in monday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                elif current_day_plus_one == 'Tuesday':
                    for i in tuesday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                elif current_day_plus_one == 'Wednesday':
                    for i in wednesday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                elif current_day_plus_one == 'Thursday':
                    for i in thursday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                elif current_day_plus_one == 'Friday':
                    for i in friday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                elif current_day_plus_one == 'Saturday':
                    for i in saturday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                elif current_day_plus_one == 'Sunday':
                    for i in sunday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                current_date_plus_one = datetime.today() + timedelta(days=2)
                current_day_plus_one = current_date_plus_one.strftime('%A')
                if current_day_plus_one == 'Monday':
                    for i in monday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                elif current_day_plus_one == 'Tuesday':
                    for i in tuesday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                elif current_day_plus_one == 'Wednesday':
                    for i in wednesday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                elif current_day_plus_one == 'Thursday':
                    for i in thursday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                elif current_day_plus_one == 'Friday':
                    for i in friday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                elif current_day_plus_one == 'Saturday':
                    for i in saturday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                elif current_day_plus_one == 'Sunday':
                    for i in sunday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                current_date_plus_one = datetime.today() + timedelta(days=3)
                current_day_plus_one = current_date_plus_one.strftime('%A')
                if current_day_plus_one == 'Monday':
                    for i in monday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                elif current_day_plus_one == 'Tuesday':
                    for i in tuesday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                elif current_day_plus_one == 'Wednesday':
                    for i in wednesday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                elif current_day_plus_one == 'Thursday':
                    for i in thursday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                elif current_day_plus_one == 'Friday':
                    for i in friday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                elif current_day_plus_one == 'Saturday':
                    for i in saturday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                elif current_day_plus_one == 'Sunday':
                    for i in sunday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                current_date_plus_one = datetime.today() + timedelta(days=4)
                current_day_plus_one = current_date_plus_one.strftime('%A')
                if current_day_plus_one == 'Monday':
                    for i in monday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                elif current_day_plus_one == 'Tuesday':
                    for i in tuesday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                elif current_day_plus_one == 'Wednesday':
                    for i in wednesday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                elif current_day_plus_one == 'Thursday':
                    for i in thursday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                elif current_day_plus_one == 'Friday':
                    for i in friday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                elif current_day_plus_one == 'Saturday':
                    for i in saturday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                elif current_day_plus_one == 'Sunday':
                    for i in sunday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                current_date_plus_one = datetime.today() + timedelta(days=5)
                current_day_plus_one = current_date_plus_one.strftime('%A')
                if current_day_plus_one == 'Monday':
                    for i in monday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                elif current_day_plus_one == 'Tuesday':
                    for i in tuesday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                elif current_day_plus_one == 'Wednesday':
                    for i in wednesday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                elif current_day_plus_one == 'Thursday':
                    for i in thursday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                elif current_day_plus_one == 'Friday':
                    for i in friday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                elif current_day_plus_one == 'Saturday':
                    for i in saturday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                elif current_day_plus_one == 'Sunday':
                    for i in sunday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                current_date_plus_one = datetime.today() + timedelta(days=6)
                current_day_plus_one = current_date_plus_one.strftime('%A')
                if current_day_plus_one == 'Monday':
                    for i in monday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                elif current_day_plus_one == 'Tuesday':
                    for i in tuesday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                elif current_day_plus_one == 'Wednesday':
                    for i in wednesday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                elif current_day_plus_one == 'Thursday':
                    for i in thursday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                elif current_day_plus_one == 'Friday':
                    for i in friday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                elif current_day_plus_one == 'Saturday':
                    for i in saturday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                elif current_day_plus_one == 'Sunday':
                    for i in sunday_time_list:
                        doc_time = doc_timing.objects.create(doctor_id=pk, day=current_day_plus_one, timing=i
                                                             , date=current_date_plus_one)
                        doc_time.save()
                obj_timing = timing_exists()
                obj_timing.doctor_id = pk
                obj_timing.status = True
                obj_timing.save()
                context = {
                    'status': 'success'
                }
                return JsonResponse(context)

            # monday_time_list = [time1_mon, time2_mon, time3_mon]
            # tuesday_time_list = [time1_tue, time2_tue, time3_tue]
            # wednesday_time_list = [time1_wed, time2_wed, time3_wed]
            # thursday_time_list = [time1_thur, time2_thur, time3_thur]
            # friday_time_list = [time1_fri, time2_fri, time3_fri]
            # saturday_time_list = [time1_sat, time2_sat, time3_sat]
            # sunday_time_list = [time1_sun, time2_sun, time3_sun]
            #
            # doc_exists = doctor.objects.filter(pk=pk).exists()
            # if doc_exists:
            #     # if monday == 'Monday':
            #     monday_exists = doc_timing.objects.filter(day='Monday').exists()
            #     if monday_exists:
            #         monday_delete = doc_timing.objects.filter(day='Monday')
            #         monday_delete.delete()
            #         for i in monday_time_list:
            #             doc_time = doc_timing.objects.create(doctor_id=pk, day='Monday', timing=i)
            #             doc_time.save()
            #     if tuesday == 'Tuesday':
            #         tuesday_exists = doc_timing.objects.filter(day=tuesday).exists()
            #         if tuesday_exists:
            #             tuesday_delete = doc_timing.objects.filter(day=tuesday)
            #             tuesday_delete.delete()
            #         for i in tuesday_time_list:
            #             doc_time = doc_timing.objects.create(doctor_id=pk, day=tuesday, timing=i)
            #             doc_time.save()
            #     if wednesday == 'Wednesday':
            #         wednesday_exists = doc_timing.objects.filter(day=wednesday).exists()
            #         if wednesday_exists:
            #             wednesday_delete = doc_timing.objects.filter(day=wednesday)
            #             wednesday_delete.delete()
            #         for i in wednesday_time_list:
            #             doc_time = doc_timing.objects.create(doctor_id=pk, day=wednesday, timing=i)
            #             doc_time.save()
            #     if thursday == 'Thursday':
            #         thursday_exists = doc_timing.objects.filter(day=thursday).exists()
            #         if thursday_exists:
            #             thursday_delete = doc_timing.objects.filter(day=thursday)
            #             thursday_delete.delete()
            #         for i in thursday_time_list:
            #             doc_time = doc_timing.objects.create(doctor_id=pk, day=thursday, timing=i)
            #             doc_time.save()
            #     if friday == 'Friday':
            #         friday_exists = doc_timing.objects.filter(day=friday).exists()
            #         if friday_exists:
            #             friday_delete = doc_timing.objects.filter(day=friday)
            #             friday_delete.delete()
            #         for i in friday_time_list:
            #             doc_time = doc_timing.objects.create(doctor_id=pk, day=friday, timing=i)
            #             doc_time.save()
            #     if saturday == 'Saturday':
            #         saturday_exists = doc_timing.objects.filter(day=saturday).exists()
            #         if saturday_exists:
            #             saturday_delete = doc_timing.objects.filter(day=saturday)
            #             saturday_delete.delete()
            #         for i in saturday_time_list:
            #             doc_time = doc_timing.objects.create(doctor_id=pk, day=saturday, timing=i)
            #             doc_time.save()
            #     if sunday == 'Sunday':
            #         sunday_exists = doc_timing.objects.filter(day=sunday).exists()
            #         if sunday_exists:
            #             sunday_delete = doc_timing.objects.filter(day=sunday)
            #             sunday_delete.delete()
            #         for i in sunday_time_list:
            #             doc_time = doc_timing.objects.create(doctor_id=pk, day=sunday, timing=i)
            #             doc_time.save()
            #         context = {
            #             'status': 'success'
            #         }
            #         return JsonResponse(context)
            #     else:
            #         context = {
            #             'status': 'failed'
            #         }
            #     return JsonResponse(context)
        except Exception as e:
            print(e)
            context = {
                'status': 'failed',
                'error': str(e)
            }
            return JsonResponse(context)


@login_required(login_url='login')
@csrf_exempt
def get_timings(request):
    try:
        pk = request.POST.get('pk')
        timing = []
        details = doctor.objects.filter(pk=pk)
        for i in details:
            timing.append({'first_time_mon': i.first_time_mon and i.first_time_mon.strftime("%I:%M"),
                           'second_time_mon': i.second_time_mon and i.second_time_mon.strftime("%I:%M"),
                           'third_time_mon': i.third_time_mon and i.third_time_mon.strftime("%I:%M"),
                           'first_time_tue': i.first_time_tue and i.first_time_tue.strftime("%I:%M"),
                           'second_time_tue': i.second_time_tue and i.second_time_tue.strftime("%I:%M"),
                           'third_time_tue': i.third_time_tue and i.third_time_tue.strftime("%I:%M"),
                           'first_time_wed': i.first_time_wed and i.first_time_wed.strftime("%I:%M"),
                           'second_time_wed': i.second_time_wed and i.second_time_wed.strftime("%I:%M"),
                           'third_time_wed': i.third_time_wed and i.third_time_wed.strftime("%I:%M"),
                           'first_time_thur': i.first_time_thur and i.first_time_thur.strftime("%I:%M"),
                           'second_time_thur': i.second_time_thur and i.second_time_thur.strftime("%I:%M"),
                           'third_time_thur': i.third_time_thur and i.third_time_thur.strftime("%I:%M"),
                           'first_time_fri': i.first_time_fri and i.first_time_fri.strftime("%I:%M"),
                           'second_time_fri': i.second_time_fri and i.second_time_fri.strftime("%I:%M"),
                           'third_time_fri': i.third_time_fri and i.third_time_fri.strftime("%I:%M"),
                           'first_time_sat': i.first_time_sat and i.first_time_sat.strftime("%I:%M"),
                           'second_time_sat': i.second_time_sat and i.second_time_sat.strftime("%I:%M"),
                           'third_time_sat': i.third_time_sat and i.third_time_sat.strftime("%I:%M"),
                           'first_time_sun': i.first_time_sun and i.first_time_sun.strftime("%I:%M"),
                           'second_time_sun': i.second_time_sun and i.second_time_sun.strftime("%I:%M"),
                           'third_time_sun': i.third_time_sun and i.third_time_sun.strftime("%I:%M")})
        context = {
            'status': 'success',
            'list': timing
        }
        return JsonResponse(context)
    except Exception as e:
        context = {
            'status': 'failed',
            'error': str(e)
        }
        return JsonResponse(context)
