from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    GROUP_CHOICES = [
        ('FUNCIONARIO', 'Funcionário'),
        ('GERENTE', 'Gerente'),
        ('CHEFE', 'Chefe'),
    ]
     
    registration = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    is_manager = models.BooleanField(default=False, null=True, blank=True)
    option = models.CharField(max_length=20, choices=GROUP_CHOICES, default='FUNCIONARIO')
    
    # problema com a criação do usuário e a senha
    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        # Define is_manager automaticamente com base no cargo
        if self.option in ['GERENTE', 'CHEFE']:
            self.is_manager = True
        else:
            self.is_manager = False

        super().save(*args, **kwargs)
