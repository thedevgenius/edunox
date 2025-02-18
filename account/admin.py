from django.contrib import admin
from .models import Role, User, TeacherProfile, StudentProfile

# Register your models here.
# admin.site.register(User)
admin.site.register(TeacherProfile)
admin.site.register(Role)

class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'username']
admin.site.register(User, UserAdmin)



class StudentProfileAdmin(admin.ModelAdmin):
    def get_user_name(self, obj):
        return obj.user.get_full_name()
    list_display = ( 'get_user_name', 'grade', 'roll')

admin.site.register(StudentProfile, StudentProfileAdmin)