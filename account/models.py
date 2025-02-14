from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Access(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=5, unique=True)
    accesses = models.ManyToManyField('Access')

    def __str__(self):
        return self.name

class User(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    BLOOD_GROUP_CHOICE = (
        ('ap', 'A +'),
        ('an', 'A -'),
        ('bp', 'B +'),
        ('bn', 'B -'),
        ('abp', 'AB +'),
        ('abn', 'AB -'),
        ('op', 'O +'),
        ('on', 'O -'),
    )
    USER_TYPE = (
        ('TE', 'Teacher'),
        ('ST', 'Student')
    )
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=5, choices=USER_TYPE, default='ST')
    date_of_birth = models.DateField(null=True)
    date_joined = models.DateField(auto_now_add=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='M')
    address = models.CharField(max_length=200, null=True)
    blood_group = models.CharField(max_length=5, null=True, choices=BLOOD_GROUP_CHOICE)
    profile_image = models.ImageField(upload_to='user/', null=True, blank=True)


    def __str__(self):
        return self.username
    
    # def save(self, *args, **kwargs):
    #     # if not self.pk:
    #     self.set_password(self.password)
    #     super().save(*args, **kwargs)

    
class TeacherProfile(models.Model):
    STATUS_CHOICE = (
        ('IO', 'In Office'),
        ('OL', 'On Leave'),
        ('ON', 'Online')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile', limit_choices_to={'role': 1})
    designation = models.CharField(max_length=200, null=True)
    core_subject = models.CharField(max_length=200, null=True)
    qualification = models.CharField(max_length=300)
    bio = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICE, default='IO')


    def __str__(self):
        return self.user.username


# class StudentProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile', editable=False, limit_choices_to={'role': 'ST'})
#     current_class = models.ForeignKey('academics.Class', on_delete=models.SET_NULL, null=True)
#     section = models.ForeignKey('academics.Section', on_delete=models.SET_NULL, null=True)
#     roll_no = models.IntegerField(null=True)

#     def __str__(self):
#         return f'{self.user.first_name} {self.user.last_name} Profile'
    


