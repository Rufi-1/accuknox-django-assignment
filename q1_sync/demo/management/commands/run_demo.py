import time
from django.core.management.base import BaseCommand
from demo.models import Item


class Command(BaseCommand):
    help = "Proves that django signals are synchronous"

    def handle(self, *args, **options):
        print("1. About to call Item.objects.create()")
        start = time.time()

        Item.objects.create(name="test item")   # this fires post_save

        end = time.time()
        print("2. create() returned")
        print("Time taken by create() = %.2f seconds" % (end - start))

        if end - start >= 5:
            print("RESULT: create() waited for the 5 sec receiver -> SYNCHRONOUS")
        else:
            print("RESULT: create() did not wait -> ASYNCHRONOUS")
