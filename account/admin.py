from django.contrib import admin
from .models import Role, Access, User, TeacherProfile

# Register your models here.
admin.site.register(Access)
admin.site.register(User)
admin.site.register(TeacherProfile)
admin.site.register(Role)

