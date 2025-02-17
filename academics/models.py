from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from account.models import StudentProfile
from django.contrib import messages

# Create your models here.
class Grade(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    
    def total_student(self):
        students = StudentProfile.objects.filter(grade=self)
        return students.count()


class Subject(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10, unique=True)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name="subjects")
    
    def __str__(self):
        return f'{self.name} - {self.code}' 

class Schedule(models.Model):
    DAY_CHOICES = (
        ('', '---'),
        ('1MN', 'Monday'),
        ('2TU', 'Tuesday'),
        ('3WD', 'Wednesday'),
        ('4TH', 'Thursday'),
        ('5FR', 'Friday'),
    )
    PERIOD_CHOICES = (
        ('', '---'),
        ('1', '1st Period'),
        ('2', '2nd Period'),
        ('3', '3rd Period'),
        ('4', '4th Period'),
        ('5', '5th Period'),
        ('6', '6th Period'),
    )
    grade = models.ForeignKey('academics.Grade', on_delete=models.CASCADE, related_name="schedules")
    day = models.CharField(max_length=5, choices=DAY_CHOICES)
    period = models.CharField(max_length=5, choices=PERIOD_CHOICES)
    subject = models.ForeignKey('academics.Subject', on_delete=models.CASCADE, related_name="schedules")
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, limit_choices_to={'type' : 'TE'})


    class Meta:
        unique_together = (('day', 'period', 'teacher'), ('day', 'period', 'grade'))

    def __str__(self):
        return f'{self.grade.name} - {self.day} {self.period} - {self.subject.name}'
