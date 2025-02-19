from django.db import models

# Create your models here.
class FeesType(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):  
        return self.name

class Fees(models.Model):
    type = models.ForeignKey(FeesType, on_delete=models.CASCADE)
    grade = models.ForeignKey('academics.Grade', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField(null=True, blank=True)
    is_monthly = models.BooleanField(default=False)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Fees'
        verbose_name_plural = 'Fees'
        unique_together = ('type', 'grade')

    def __str__(self):
        return f'{self.type} - {self.grade}'