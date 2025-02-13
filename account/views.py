from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.db.models import Count
from datetime import datetime
from .forms import LoginForm, AddTeacherForm, AddStudentForm
from .models import TeacherProfile, User, StudentProfile
from academics.models import Class, Section

now = datetime.now()
# Create your views here.

class SignInView(LoginView):
    template_name = 'account/login.html'
    redirect_authenticated_user = True
    form_class = LoginForm


def logout_view(request):
    logout(request)
    return redirect('home')

class TeacherListView(LoginRequiredMixin, TemplateView):
    template_name = 'account/teacher_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teachers = User.objects.filter(role='TE').select_related('teacher_profile')
        context.update({
            'teachers': teachers,
            'total_teacher': teachers.count()
        })
        return context

    
class AddTeacherView(TemplateView):
    template_name = 'account/teacher_add.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AddTeacherForm()
        
        return context
    

    def post(self, request, *args, **kwargs):
        form = AddTeacherForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = User.objects.create_user(username=username,
                                            password='Summer@2025#',
                                            first_name = form.cleaned_data.get('first_name'),
                                            last_name = form.cleaned_data.get('last_name'),
                                            email = form.cleaned_data.get('email'))
            user.role = 'TE'
            user.save()
            teacher_profile = TeacherProfile.objects.create(user=user, )
            teacher_profile.bio = form.cleaned_data.get('bio')
            teacher_profile.qualification = form.cleaned_data.get('qualification')
            teacher_profile.save()
            return redirect('teachers')
        else:
            print('Error')
        return render(request, self.template_name, {'form': form})
    

class AddStudentView(TemplateView):
    template_name = 'account/student_add.html'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AddStudentForm()

        return context
    
    def post(self, request, *args, **kwargs):
        form = AddStudentForm(request.POST, request.FILES)
        if form.is_valid():
            current_class = form.cleaned_data.get('current_class')
            first_name=form.cleaned_data.get('first_name')
            last_name=form.cleaned_data.get('last_name')
            dob = form.cleaned_data.get('dob')
            profile_image=form.cleaned_data.get('profile_image')
            username = f'EDU{str(now.year)[2:]}{first_name[:1]}{last_name[:1]}{dob.month:02}{dob.day:02}'
            user = User.objects.create_user(
                username=username,
                password='Summer@2025#',
                first_name=first_name,
                last_name=last_name,
                email=form.cleaned_data.get('email'),
                phone=form.cleaned_data.get('phone'),
                address=form.cleaned_data.get('address'),
                dob=dob,
                profile_image=profile_image
            )
            
            #Create student profile for student
            student_profile = StudentProfile.objects.create(
                user=user,
                current_class=current_class,    
            )

            #Assign available section to student
            sections = Section.objects.filter(class_obj=current_class).annotate(student_count=Count('studentprofile'))
            for section in sections:
                if section.student_count < section.max_student:
                    student_profile.section = section
                    student_profile.save()
                    break
            return redirect('teachers')
        else:
            print('Error')
        return render(request, self.template_name, {'form': form})