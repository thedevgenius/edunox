from django.db import models
from django.contrib.auth.models import AbstractUser, Permission

# Create your models here.

# class Access(models.Model):
#     name = models.CharField(max_length=200)
#     code = models.CharField(max_length=200, unique=True)

#     def __str__(self):
#         return self.name

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    permissions = models.ManyToManyField(Permission, blank=True)

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
        ('ST', 'Student'),
        ('AD', 'Admin'),
    )
    CASTE_CHOICE = (
        ('GN', 'General'),
        ('SC', 'SC'),
        ('ST', 'ST'),
        ('OB', 'OBC'),
    )
    RELIGION_CHOICE = (
        ('H', 'Hindu'),
        ('M', 'Muslim'),
        ('S', 'Sikh'),
        ('O', 'Other')
    )
    
    role = models.ManyToManyField(Role, blank=True)
    type = models.CharField(max_length=5, choices=USER_TYPE, default='ST')
    date_of_birth = models.DateField(null=True)
    date_joined = models.DateField(auto_now_add=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='M')
    address = models.CharField(max_length=200, null=True)
    blood_group = models.CharField(max_length=5, null=True, choices=BLOOD_GROUP_CHOICE)
    profile_image = models.ImageField(upload_to='user/', null=True, blank=True)
    caste = models.CharField(max_length=5, null=True, choices=CASTE_CHOICE)
    religion = models.CharField(max_length=5, null=True, choices=RELIGION_CHOICE)


    def __str__(self):
        return self.get_full_name()
    
    # def save(self, *args, **kwargs):
    #     # if not self.pk:
    #     self.set_password(self.password)
    #     super().save(*args, **kwargs)

    def has_permission(self, perm_codename):
        """Check if user has a specific permission."""
        return self.role.filter(permissions__codename=perm_codename).exists()
    def has_role(self, role_name):
        return self.role.filter(name=role_name).exists()

    

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


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile', editable=False, limit_choices_to={'role': 'ST'})
    grade = models.ForeignKey('academics.Grade', on_delete=models.SET_NULL, null=True)
    roll = models.IntegerField(null=True)
    total_roll = models.IntegerField(null=True)
    father_name = models.CharField(max_length=200, null=True)
    father_email = models.EmailField(null=True)
    father_phone = models.CharField(max_length=15, null=True)
    mother_name = models.CharField(max_length=200, null=True)
    mother_email = models.EmailField(null=True)
    mother_phone = models.CharField(max_length=15, null=True)
    
    

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} Profile'
    


