from django.db import models
from django.contrib.auth.models import User

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
