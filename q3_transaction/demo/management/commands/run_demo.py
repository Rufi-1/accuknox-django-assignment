from django.core.management.base import BaseCommand
from django.db import transaction
from demo.models import Item, Log


class Command(BaseCommand):
    help = "Proves that django signals run in the same DB transaction as the caller"

    def handle(self, *args, **options):
        print("Before: Items =", Item.objects.count(), "| Logs =", Log.objects.count())

        # We open a transaction, save an Item (signal creates a Log),
        # and then raise an error on purpose so the transaction rolls back.
        try:
            with transaction.atomic():
                Item.objects.create(name="rollback test")
                print("   [caller] inside atomic: Items =", Item.objects.count(),
                      "| Logs =", Log.objects.count())
                raise Exception("forcing a rollback")
        except Exception as e:
            print("Caught error:", e)

        items = Item.objects.count()
        logs = Log.objects.count()
        print("After rollback: Items =", items, "| Logs =", logs)

        # If the signal had its own separate transaction, the Log row would
        # have been committed and would still exist here.
        if logs == 0:
            print("RESULT: Log row was ALSO rolled back -> SAME TRANSACTION")
        else:
            print("RESULT: Log row survived -> DIFFERENT TRANSACTION")
