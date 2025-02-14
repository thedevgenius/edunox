from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.db.models import Count
from datetime import datetime
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, AddTeacherForm, AddStudentForm
from .models import TeacherProfile, User, Role


now = datetime.now()
# # Create your views here.

class SignInView(LoginView):
    template_name = 'account/login.html'
    redirect_authenticated_user = True
    form_class = LoginForm


def logout_view(request):
    logout(request)
    return redirect('home')

@method_decorator(login_required, name='dispatch')
class TeacherListView(LoginRequiredMixin, TemplateView):
    template_name = 'account/teacher_list.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.role.accesses.filter(name='View Teacher').exists():
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teachers = User.objects.filter(type='TE').select_related('teacher_profile').order_by('first_name')

        context.update({
            'teachers': teachers,
            'total_teacher': teachers.count()
        })
        return context

@method_decorator(login_required, name='dispatch')
class AddTeacherView(TemplateView):
    template_name = 'account/teacher_add.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.role.accesses.filter(name='Add Teacher').exists():
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AddTeacherForm()
        
        return context
    

    def post(self, request, *args, **kwargs):
        form = AddTeacherForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            dob = form.cleaned_data.get('date_of_birth')
            username = f'TE{str(now.year)[2:]}{first_name[:1]}{last_name[:1]}{dob.month:02}{dob.day:02}'
            role, _ = Role.objects.get_or_create(name='Teacher')
            user = User.objects.create_user(
                username=username,
                password='Summer@2025#',
                first_name = first_name,
                last_name = last_name,
                email = form.cleaned_data.get('email'),
                blood_group=form.cleaned_data.get('blood_group'),
                gender=form.cleaned_data.get('gender'),
                address=form.cleaned_data.get('address'),
                date_of_birth=form.cleaned_data.get('date_of_birth'),
                profile_image=form.cleaned_data.get('profile_image'),
                role=role,
                type='TE'
            )
            teacher_profile = TeacherProfile.objects.create(
                user=user,
                designation=form.cleaned_data.get('designation'),
                core_subject=form.cleaned_data.get('core_subject'),
                qualification=form.cleaned_data.get('qualification'),
                bio=form.cleaned_data.get('bio'),
            )
            return redirect('teacher_list')
        else:
            print('Error')
        return render(request, self.template_name, {'form': form})
    
class TeacherDetailsView(DetailView):
    model = User
    template_name = 'account/teacher_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teacher = self.get_object()
        context['teacher'] = teacher
        return context

# class AddStudentView(TemplateView):
#     template_name = 'account/student_add.html'

    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = AddStudentForm()

#         return context
    
#     def post(self, request, *args, **kwargs):
#         form = AddStudentForm(request.POST, request.FILES)
#         if form.is_valid():
#             current_class = form.cleaned_data.get('current_class')
#             first_name=form.cleaned_data.get('first_name')
#             last_name=form.cleaned_data.get('last_name')
#             dob = form.cleaned_data.get('dob')
#             profile_image=form.cleaned_data.get('profile_image')
#             username = f'EDU{str(now.year)[2:]}{first_name[:1]}{last_name[:1]}{dob.month:02}{dob.day:02}'
#             user = User.objects.create_user(
#                 username=username,
#                 password='Summer@2025#',
#                 first_name=first_name,
#                 last_name=last_name,
#                 email=form.cleaned_data.get('email'),
#                 phone=form.cleaned_data.get('phone'),
#                 address=form.cleaned_data.get('address'),
#                 dob=dob,
#                 profile_image=profile_image
#             )
            
#             #Create student profile for student
#             student_profile = StudentProfile.objects.create(
#                 user=user,
#                 current_class=current_class,    
#             )

#             #Assign available section to student
#             sections = Section.objects.filter(class_obj=current_class).annotate(student_count=Count('studentprofile'))
#             for section in sections:
#                 if section.student_count < section.max_student:
#                     student_profile.section = section
#                     student_profile.save()
#                     break
#             return redirect('teachers')
#         else:
#             print('Error')
#         return render(request, self.template_name, {'form': form})