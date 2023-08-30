from django.db import models

# Create your models here.

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'

class JobApplication(models.Model):
    APPROVAL_STATUSES = (
        (0, 'Ожидает одобрения'),
        (1, 'Одобрено'),
        (2, 'Отклонено'),
    ) 
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = PhoneNumberField()
    birtday = models.DateField(blank=False)
    resume = models.FileField(upload_to='resumes/')
    gender = models.CharField(max_length=1, choices=Gender.choices)
    approval_status = models.CharField(max_length=20, choices=APPROVAL_STATUSES, default='pending')
    job = models.ForeignKey('Job', on_delete=models.CASCADE, null=True)
    current_admin_stage  = models.PositiveIntegerField(default=2)

    def __str__(self):
        return self.first_name
    
class Job(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True)
    
    def __str__(self):
        return self.title