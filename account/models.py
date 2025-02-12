from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = (
        ('ST', 'Student'),
        ('TE', 'Teacher'),
    )
    phone = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=2, choices=ROLE_CHOICES, default='ST')

    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.set_password(self.password)
        super().save(*args, **kwargs)

    
class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile', editable=False)
    academic_qualification = models.CharField(max_length=300)
    bio = models.TextField()
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
