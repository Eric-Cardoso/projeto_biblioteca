from datetime import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Client


@receiver(post_save, sender=Client)
def update_expiration_date(sender, instance, created, **kwargs):
    if created:
        if not instance.expiration_date:
            current_date = datetime.now()
            expiration_date = current_date.replace(
                year=current_date.year + 1,
            )
            Client.objects.filter(pk=instance.pk).update(
                expiration_date=expiration_date
            )
