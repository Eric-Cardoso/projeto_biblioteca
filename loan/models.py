from django.db import models

from book.models import Book
from client.models import Client


class LoanDuration(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Nome',
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Descrição',
    )

    class Meta:
        verbose_name = 'Duração de empréstimo'
        verbose_name_plural = 'Durações de empréstimo'

    def __str__(self):
        return self.name


class Loan(models.Model):
    client = models.ForeignKey(
        Client,
        on_delete=models.PROTECT,
        related_name='loans',
        verbose_name='Cliente',
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.PROTECT,
        related_name='loans',
        verbose_name='Livro',
    )
    loan_date = models.DateField(
        auto_now_add=True,
        verbose_name='Data do empréstimo',
    )
    loan_duration = models.ForeignKey(
        LoanDuration,
        on_delete=models.PROTECT,
        related_name='loans',
        verbose_name='Duração do empréstimo',
    )
    devolution_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Data de devolução',
    )

    class Meta:
        verbose_name = 'Empréstimo'
        verbose_name_plural = 'Empréstimos'

    def __str__(self):
        return (
            f'{self.client.name} - {self.book.name} '
            f'- {self.loan_date} - {self.loan_duration}'
        )
