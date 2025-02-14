from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Grade(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name


    
    
# class Section(models.Model):
#     grade = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="sections")
#     name = models.CharField(max_length=5)
#     class_teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'role' : 'TE'})
#     max_student = models.IntegerField(default=40)

#     def __str__(self):
#         return f"{self.class_obj.name} - Section {self.name}"

# class Subject(models.Model):
#     name = models.CharField(max_length=50)
#     code = models.CharField(max_length=10, unique=True)
#     class_obj = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="subjects")
    
#     def __str__(self):
#         return self.code
