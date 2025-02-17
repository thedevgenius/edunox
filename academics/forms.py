from django import forms
from .models import Schedule, Subject
from account.models import User


class AddScheduleForm(forms.Form):
    DAY_CHOICES = (
        ('', '---'),
        ('MN', 'Monday'),
        ('TU', 'Tuesday'),
        ('WD', 'Wednesday'),
        ('TH', 'Thursday'),
        ('FR', 'Friday'),
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
    day = forms.ChoiceField(choices=DAY_CHOICES, widget=forms.Select(attrs={'class': 'select'}))
    period = forms.ChoiceField(choices=PERIOD_CHOICES, widget=forms.Select(attrs={'class': 'select'}))
    subject = forms.ModelChoiceField(queryset=Subject.objects.none(), widget=forms.Select(attrs={'class': 'select'}))
    teacher = forms.ModelChoiceField(queryset=User.objects.filter(type='TE'), widget=forms.Select(attrs={'class': 'select'}))

    class Meta:
        model = Schedule
        fields = ['day', 'period', 'subject', 'teacher']

    def __init__(self, grade, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subject'].queryset = Subject.objects.filter(grade=grade)