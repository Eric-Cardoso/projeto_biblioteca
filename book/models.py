from django.db import models


class BookGenre(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Nome',
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Descrição',
    )

    class Meta:
        verbose_name = 'Gênero literário'
        verbose_name_plural = 'Gêneros literários'

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Nome',
    )
    author = models.CharField(
        max_length=50,
        verbose_name='Autor',
    )
    genre = models.ForeignKey(
        BookGenre,
        on_delete=models.PROTECT,
        related_name='books',
        verbose_name='Gênero',
    )
    isbn = models.CharField(
        max_length=25,
        unique=True,
        verbose_name='ISBN',
    )
    was_loaned = models.BooleanField(
        default=False,
        verbose_name='Está emprestado',
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Descrição',
    )
    publication_date = models.DateField(
        verbose_name='Data de publicação',
    )

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'

    def __str__(self):
        return f'{self.name} - {self.author} - {self.publication_date}'
