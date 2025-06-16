from django.db import models


# Create your models here.

class doctor(models.Model):
    name = models.TextField(default='')
    qualification = models.TextField(default='')
    number = models.TextField(default='')
    image = models.TextField(default='')
    country = models.TextField(default='')
    workspace = models.TextField(default='')
    email = models.TextField(default='')
    first_time_mon = models.TimeField(null=True, blank=True)
    second_time_mon = models.TimeField(null=True, blank=True)
    third_time_mon = models.TimeField(null=True, blank=True)
    first_time_tue = models.TimeField(null=True, blank=True)
    second_time_tue = models.TimeField(null=True, blank=True)
    third_time_tue = models.TimeField(null=True, blank=True)
    first_time_wed = models.TimeField(null=True, blank=True)
    second_time_wed = models.TimeField(null=True, blank=True)
    third_time_wed = models.TimeField(null=True, blank=True)
    first_time_thur = models.TimeField(null=True, blank=True)
    second_time_thur = models.TimeField(null=True, blank=True)
    third_time_thur = models.TimeField(null=True, blank=True)
    first_time_fri = models.TimeField(null=True, blank=True)
    second_time_fri = models.TimeField(null=True, blank=True)
    third_time_fri = models.TimeField(null=True, blank=True)
    first_time_sat = models.TimeField(null=True, blank=True)
    second_time_sat = models.TimeField(null=True, blank=True)
    third_time_sat = models.TimeField(null=True, blank=True)
    first_time_sun = models.TimeField(null=True, blank=True)
    second_time_sun = models.TimeField(null=True, blank=True)
    third_time_sun = models.TimeField(null=True, blank=True)

class visitor_count(models.Model):
    v_count = models.IntegerField(default=0)


class apply_as_doctor(models.Model):
    name = models.TextField(default='')
    qualification = models.TextField(default='')
    city = models.TextField(default='')
    country = models.TextField(default='')
    number = models.TextField(default='')
    email = models.TextField(default='')
    status = models.BooleanField(default=False)
