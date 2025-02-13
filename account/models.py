from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = (
        ('ST', 'Student'),
        ('TE', 'Teacher'),
    )
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    phone = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=2, choices=ROLE_CHOICES, default='ST')
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, null=True)
    address = models.CharField(max_length=300, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    dob = models.DateField(null=True, verbose_name='Date of Birth')
    profile_image = models.ImageField(upload_to='user/', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.set_password(self.password)
        

        super().save(*args, **kwargs)

    
class TeacherProfile(models.Model):
    STATUS_CHOICE = (
        ('IO', 'In Office'),
        ('OL', 'On Leave'),
        ('ON', 'Online')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile', editable=False)
    designation = models.CharField(max_length=200, null=True)
    core_subject = models.CharField(max_length=200, null=True)
    qualification = models.CharField(max_length=300)
    bio = models.TextField()
    status = models.CharField(max_length=2, choices=STATUS_CHOICE, default='IO')


    def __str__(self):
        return self.user.username


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile', editable=False, limit_choices_to={'role': 'ST'})
    from academics.models import Class, Section
    current_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)
    roll_no = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} Profile'
    
