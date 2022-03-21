import time

from django.db import connections

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    #  Command class inherit from BaseCommand
    """Django command to pause execuion until database is available"""
    def handle(self, *args, **options):
        self.stdout.write('waiting for database ...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                #  printing to screen for users
                self.stdout.write('Database unavailable, waiting for 1 second..')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available'))
