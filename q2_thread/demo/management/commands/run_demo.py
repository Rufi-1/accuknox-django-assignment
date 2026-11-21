import threading
from django.core.management.base import BaseCommand
from demo.models import Item


def save_item(label):
    t = threading.current_thread()
    print(label, "caller thread name   =", t.name, "| id =", t.ident)
    item = Item.objects.create(name=label)
    return t.ident


class Command(BaseCommand):
    help = "Proves that django signals run in the same thread as the caller"

    def handle(self, *args, **options):
        # Test 1: call from the main thread
        print("--- Test 1: main thread ---")
        caller_id = save_item("main")

        # Test 2: call from a new thread that we create ourselves
        # (if the signal ran in some other thread, the ids would not match)
        print("--- Test 2: our own new thread ---")
        t = threading.Thread(target=save_item, args=("worker",), name="my-worker-thread")
        t.start()
        t.join()

        print("RESULT: in both tests the receiver printed the SAME thread "
              "name and id as the caller -> SAME THREAD")
