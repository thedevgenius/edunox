from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User

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
    
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Email'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True, widget=forms.RadioSelect(attrs={'class': 'radio'}))
    address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Address'}))
    date_of_birth = forms.DateField(label='Date of Birth', widget=forms.DateInput(attrs={'type': 'date', 'class': 'input'}))
    blood_group = forms.ChoiceField(choices=BLOOD_GROUP_CHOICE, required=True, widget=forms.Select(attrs={'class': 'select'}))
    profile_image = forms.ImageField(widget=forms.FileInput())
    

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
    username = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Username'}))
    # current_class = forms.ModelChoiceField(queryset=Class.objects.all(), widget=forms.Select(attrs={'class': 'select'}))

