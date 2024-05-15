from django.core.management import BaseCommand
from core.models import Author
from django.db import transaction


class Command(BaseCommand):

    def handle(self, *args, **options):
        authors = Author.objects.all()
        with transaction.atomic():
            for author in authors:
                if author.name:
                    last_name = author.name.split(" ")[-1]
                    author.last_name = last_name
                    author.save()
                    print(last_name)



