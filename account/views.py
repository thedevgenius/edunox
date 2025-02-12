from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.db.models import Count
from .forms import LoginForm, AddTeacherForm
from .models import TeacherProfile, User


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
            teacher_profile.academic_qualification = form.cleaned_data.get('academic_qualification')
            teacher_profile.save()
            return redirect('teachers')
        else:
            print('Error')
        return render(request, self.template_name, {'form': form})
    