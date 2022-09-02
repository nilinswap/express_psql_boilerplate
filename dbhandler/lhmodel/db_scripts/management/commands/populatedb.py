from django.core.management.base import BaseCommand, CommandError
from db_scripts import populatedb

class Command(BaseCommand):
    help = 'populates db'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        populatedb.populatedb()
