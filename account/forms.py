from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from academics.models import Class

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class UserAddForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Username'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Email'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Phone Number'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True, widget=forms.RadioSelect(attrs={'class': 'radio'}))
    address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Address'}))
    dob = forms.DateField(label='Date of Birth', widget=forms.DateInput(attrs={'type': 'date', 'class': 'input'}))
    profile_image = forms.ImageField(widget=forms.FileInput())
    

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'dob']


class AddTeacherForm(UserAddForm):
    qualification = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Academic Qualification'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'Bio'}))


class AddStudentForm(UserAddForm):
    username = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Username'}))
    current_class = forms.ModelChoiceField(queryset=Class.objects.all(), widget=forms.Select(attrs={'class': 'select'}))

