from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.generic import View
User = get_user_model()
from academics.models import Schedule
from datetime import datetime

def get_day_for_schedule(text):
    if text == 'Tue':
        return '2TU'

# Create your views here.
class HomeView(TemplateView):
    template_name = 'core/index.html'

@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = 'core/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.has_role('Admin'):
            students = User.objects.filter(type='ST', is_active=True).only('id', 'gender')
            context['total_student'] = students.count()
            context['total_male_student'] = students.filter(gender='M').count()
            context['total_female_student'] = students.filter(gender='F').count()
            context['total_other_student'] = students.filter(gender='O').count()
        if self.request.user.has_role('Teacher'):
            now = datetime.now()
            day = get_day_for_schedule(now.strftime('%a'))
            context['schedules'] = Schedule.objects.filter(day=day, teacher=self.request.user)
            


        return context
    

def get_student_by_gender(request):
    students = User.objects.filter(type='ST', is_active=True).only('id', 'gender')
    total_student = students.count()
    total_male_student = students.filter(gender='M').count()
    total_female_student = students.filter(gender='F').count()
    total_other_student = students.filter(gender='O').count()

    data = {
        'labels' : ['Male', 'Female', 'Other'],
        'values' : [total_male_student, total_female_student, total_other_student],
        'colors' : ['#b91d47', '#00aba9', '#2b5797']
    }
    return JsonResponse(data)

