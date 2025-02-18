from collections import defaultdict
from datetime import datetime

from django.shortcuts import redirect
from django.contrib import messages
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, View

from account.models import StudentProfile, User
from .forms import AddScheduleForm
from .models import Grade, Subject, Schedule, Attendance


# Create your views here.
class ClassListView(TemplateView):
    template_name = 'academics/class_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        grades = Grade.objects.all()
        context['grades'] = grades
        return context


class ClassDetailView(DetailView):
    model = Grade
    template_name = 'academics/class_detail.html'
    context_object_name = 'class'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        grade = Grade.objects.get(id=self.kwargs['pk'])
        context['students'] = StudentProfile.objects.filter(grade=grade).order_by('roll')
        context['subjects'] = Subject.objects.filter(grade=grade)
        context['form'] = AddScheduleForm(grade=grade)
        
        schedules = Schedule.objects.filter(grade=grade).select_related('grade', 'subject', 'teacher').order_by('day', 'period')
        grouped_schedules = defaultdict(list)
        for schedule in schedules:
            grouped_schedules[schedule.day].append(schedule)
        context['grouped_schedules'] = dict(grouped_schedules)

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = AddScheduleForm(self.object, request.POST)
        if form.is_valid():
            try:
                Schedule.objects.create(
                    grade=self.object,
                    day=form.cleaned_data.get('day'),
                    subject=form.cleaned_data.get('subject'),
                    period=form.cleaned_data.get('period'),
                    teacher=form.cleaned_data.get('teacher'),
                )
            except IntegrityError:
                messages.error(request, 'Schedule already exists for the selected day and period.', extra_tags='danger')
        else:
            print(form.errors)
        return self.get(request, *args, **kwargs) 

class AddAttendanceView(TemplateView):
    template_name = 'academics/attendance_add.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = Grade.objects.get(id=self.kwargs['pk'])
        context['students'] = StudentProfile.objects.filter(grade=context['class']).order_by('total_roll')
        return context
    
    def post(self, request, *args, **kwargs):
        students = User.objects.filter(student_profile__grade=Grade.objects.get(id=self.kwargs['pk']))
        now = datetime.now()
        attendance = []
        attendance_data = {}

        for student in students:
            checkbox_value = request.POST.get(f"att_{student.id}", "0")
            attendance_data[student.id] = True if checkbox_value == "1" else False
        print("Attendance Data:", attendance_data)
            # status = True if att == "on" else False
            # print(student, status)
            # attendance.append(Attendance(date=now, student=student, status=status))
        # Attendance.objects.bulk_create(attendance)
        return redirect('dashboard')