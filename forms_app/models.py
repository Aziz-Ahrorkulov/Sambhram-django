from django.db import models

# Create your models here.

from django.db import models

class Gender(models.TextChoices):
    MALE = 'M', 'Male'
    FEMALE = 'F', 'Female'
    OTHER = 'O', 'Other'

class JobApplication(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    birtday = models.DateField(blank=False)
    resume = models.FileField(upload_to='resumes/')
    gender = models.CharField(max_length=1, choices=Gender.choices)

    def __str__(self):
        return self.first_name