from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    registration = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    is_manager = models.BooleanField(default=False, null=True, blank=True)
    
    # problema com a criação do usuário e a senha
    def __str__(self):
        return self.username
    
class UserGroup(models.Model):
    GROUP = [
        ('FUNCIONARIO', 'Funcionário'),
        ('GERENTE', 'Gerente'),
        ('CHEFE', 'Chefe'),
    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    option = models.CharField(max_length=20, choices=GROUP, default='FUNCIONARIO')

    def __str__(self):
        return f"{self.user.username}"
