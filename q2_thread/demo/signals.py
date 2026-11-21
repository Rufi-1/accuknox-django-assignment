import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Item


@receiver(post_save, sender=Item)
def my_receiver(sender, instance, created, **kwargs):
    # print the thread this receiver is running in
    t = threading.current_thread()
    print("   [signal] receiver thread name =", t.name, "| id =", t.ident)
