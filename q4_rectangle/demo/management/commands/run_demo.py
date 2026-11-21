from django.core.management.base import BaseCommand
from demo.rectangle import Rectangle


class Command(BaseCommand):
    help = "Shows how the Rectangle class can be iterated over"

    def handle(self, *args, **options):
        rect = Rectangle(10, 5)

        print("Looping over Rectangle(10, 5):")
        for item in rect:
            print("  ", item)

        print("As a list:", list(rect))

        # checking the order: length first, then width
        result = list(rect)
        if result == [{'length': 10}, {'width': 5}]:
            print("RESULT: length came first, then width -> CORRECT")
        else:
            print("RESULT: something is wrong")
