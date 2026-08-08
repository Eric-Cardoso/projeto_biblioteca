from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from book.models import Book

from .models import Loan


@receiver(post_save, sender=Loan)
def update_book_status_post_save(
    sender,
    instance,
    created,
    **kwargs,
):
    if created:
        if instance.devolution_date:
            Loan.objects.filter(pk=instance.pk).update(
                devolution_date=None,
            )

        Book.objects.filter(pk=instance.book.pk).update(
            was_loaned=True,
        )
    elif instance.devolution_date:
        Book.objects.filter(pk=instance.book.pk).update(
            was_loaned=False,
        )


@receiver(post_delete, sender=Loan)
def update_book_status_post_delete(
    sender,
    instance,
    **kwargs,
):
    Book.objects.filter(pk=instance.book.pk).update(
        was_loaned=False,
    )
