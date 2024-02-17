from django.core.management.base import BaseCommand
from myclub.models import Products 

class Command(BaseCommand):
    help = 'Prints the number of products in the database'

    def handle(self, *args, **options):
        count = Products.objects.count()
        self.stdout.write(self.style.SUCCESS(f'Number of products: {count}'))

        