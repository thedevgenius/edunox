from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from academics.models import Grade

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class UserAddForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    BLOOD_GROUP_CHOICE = [
        ('', 'Select Blood group'),
        ('ap', 'A +'),
        ('an', 'A -'),
        ('bp', 'B +'),
        ('bn', 'B -'),
        ('abp', 'AB +'),
        ('abn', 'AB -'),
        ('op', 'O +'),
        ('on', 'O -'),
    ]
    CASTE_CHOICE = [
        ('', 'Select Caste'),
        ('GN', 'General'),
        ('SC', 'SC'),
        ('ST', 'ST'),
        ('OB', 'OBC'),
    ]
    RELIGION_CHOICE = [
        ('', 'Select Religion'),
        ('H', 'Hindu'),
        ('M', 'Muslim'),
        ('S', 'Sikh'),
        ('O', 'Other')
    ]
    
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Email'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True, widget=forms.RadioSelect(attrs={'class': 'radio'}))
    address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Address'}))
    date_of_birth = forms.DateField(label='Date of Birth', widget=forms.DateInput(attrs={'type': 'date', 'class': 'input'}))
    blood_group = forms.ChoiceField(choices=BLOOD_GROUP_CHOICE, required=True, widget=forms.Select(attrs={'class': 'select'}))
    profile_image = forms.ImageField(required=False, widget=forms.FileInput())
    caste = forms.ChoiceField(choices=CASTE_CHOICE, required=True, widget=forms.Select(attrs={'class': 'select'}))
    religion = forms.ChoiceField(choices=RELIGION_CHOICE, required=True, widget=forms.Select(attrs={'class': 'select'}))
    

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class AddTeacherForm(UserAddForm):
    username = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Username'}))
    designation = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'e.g. Senior Teacher'}))
    qualification = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'e.g. B. Sc., M. Sc.'}))
    core_subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'e.g. Physics'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'e.g. Sample bio'}))



class AddStudentForm(UserAddForm):
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Email'}))
    username = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Username'}))
    grade = forms.ModelChoiceField(label='Class', queryset=Grade.objects.all(), widget=forms.Select(attrs={'class': 'select'}))
    father_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Father Name'}))
    father_email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Father Email'}))
    father_phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Father Phone'}))
    mother_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Mother Name'}))
    mother_email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Mother Email'}))
    mother_phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Mother Phone'}))