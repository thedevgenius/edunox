from django.contrib import admin
from .models import Grade, Subject, Schedule, Attendance

# Register your models here.

admin.site.register(Grade)
admin.site.register(Subject)
# admin.site.register(Schedule)  

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['date', 'student', 'status']

admin.site.register(Attendance, AttendanceAdmin)

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['day', 'period', 'teacher']
admin.site.register(Schedule, ScheduleAdmin)