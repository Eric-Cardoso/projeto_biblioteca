from django.contrib.auth.models import User
from django.db import models

class Client(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True, 
        related_name='client', 
        verbose_name='Usuário',
    )

    name = models.CharField(max_length=50, verbose_name='Nome',)
    cpf = models.CharField(max_length=25, unique=True, verbose_name='CPF',)
    phone = models.CharField(
        max_length=25, 
        null=True, 
        blank=True, 
        unique=True,
        verbose_name='Telefone',
    )
    issue_date = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Data de emissão',
    )
    expiration_date = models.DateTimeField(
        null=True, 
        blank=True, 
        verbose_name='Data de expiração',
    )

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.name

    
