from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from forms_app.models import Job

class AdminProfile(models.Model):
    ADMIN_ROLES = (
        (1, 'Админ'),
        (2, 'Администратор 1'),
        (3, 'Администратор 2'),
        (4, 'Администратор 3'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    role = models.PositiveIntegerField(choices=ADMIN_ROLES)

    def __str__(self):
        return self.user.username
        
    class Meta:
        verbose_name = 'Админ'
        verbose_name_plural = 'Админы'

# Create your models here.

class Gender(models.TextChoices):
    MALE = 'M', 'Male'
    FEMALE = 'F', 'Female'

class Workers(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = PhoneNumberField()
    birtday = models.DateField(blank=False)
    gender = models.CharField(max_length=1, choices=Gender.choices)
    job = models.ForeignKey(Job, related_name='jobs', on_delete=models.CASCADE, null=True)