from django.contrib import admin
from .models import Grade, Subject, Schedule

# Register your models here.

admin.site.register(Grade)
admin.site.register(Subject)
admin.site.register(Schedule)  