import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Item


@receiver(post_save, sender=Item)
def slow_receiver(sender, instance, created, **kwargs):
    # This receiver is made slow ON PURPOSE (sleeps 5 seconds)
    print("   [signal] receiver started")
    time.sleep(5)
    print("   [signal] receiver finished")
