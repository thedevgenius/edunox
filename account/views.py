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
from .models import TeacherProfile, StudentProfile, User, Role


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


@method_decorator(login_required, name='dispatch')
class TeacherDetailsView(DetailView):
    model = User
    template_name = 'account/teacher_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teacher = self.get_object()
        context['teacher'] = teacher
        return context


@method_decorator(login_required, name='dispatch')
class AddStudentView(TemplateView):
    template_name = 'account/student_add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AddStudentForm()

        return context
    
    def post(self, request, *args, **kwargs):
        form = AddStudentForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            dob = form.cleaned_data.get('date_of_birth')
            username = f'ST{now.strftime("%y")}{first_name[0]}{last_name[0]}{dob:%m%d}'
            role, _ = Role.objects.get_or_create(name='Student')

            user = User.objects.create_user(
                username=username,
                password='Summer@2025#',
                first_name=first_name,
                last_name=last_name,
                blood_group=form.cleaned_data.get('blood_group'),
                gender=form.cleaned_data.get('gender'),
                address=form.cleaned_data.get('address'),
                date_of_birth=form.cleaned_data.get('date_of_birth'),
                profile_image=form.cleaned_data.get('profile_image'),
                role=role,
                type='ST'
            )
            grade = form.cleaned_data.get('grade')
            last_roll = StudentProfile.objects.filter(grade=grade).aggregate(last_roll=Count('roll'))['last_roll'] or 0
            total_roll = last_roll + 1
            StudentProfile.objects.create(
                user=user,
                grade=grade,
                total_roll=total_roll,
                father_name=form.cleaned_data.get('father_name'),
                father_email=form.cleaned_data.get('father_email'),
                father_phone=form.cleaned_data.get('father_phone'),
                mother_name=form.cleaned_data.get('mother_name'),
                mother_email=form.cleaned_data.get('mother_email'),
                mother_phone=form.cleaned_data.get('mother_phone'),
            )
            return redirect('dashboard')

        else:
            print('Error')
        return render(request, self.template_name, {'form': form})
    
@method_decorator(login_required, name='dispatch')
class StudentListView(TemplateView):
    template_name = 'account/student_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        students = User.objects.filter(type='ST').select_related('student_profile').order_by('first_name')
        
        context.update({
           'students': students,
            'total_student': students.count()
        })
        return context



@method_decorator(login_required, name='dispatch')
class StudentDetailsView(DetailView):
    model = User
    template_name = 'account/student_detail.html'
    context_object_name = 'student'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = self.get_object()
        context['student'] = student
        return context