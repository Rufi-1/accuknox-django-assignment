from django.db import connection
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Item, Log


@receiver(post_save, sender=Item)
def make_log(sender, instance, created, **kwargs):
    # is the receiver running inside a transaction opened by the caller?
    print("   [signal] in_atomic_block =", connection.in_atomic_block)
    Log.objects.create(message="saved " + instance.name)
    print("   [signal] Log row created")
