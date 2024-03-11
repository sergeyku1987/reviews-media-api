from django.core.management.base import BaseCommand, CommandParser
from pathlib import Path
import os


class Command(BaseCommand):

    def  handle(self, *args, **options):
        dr = options.get('name_dir')[0]
        fl = options.get('name_file')[0]
        pt = ''
        for path, dirname, _ in os.walk(Path.cwd()):
            print('---')
            if dr in dirname:
                pt = Path(path) / dr
                break
        for file in os.listdir(pt):
            if file == fl:
                print('find')
                break
        

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('name_dir', nargs='+', type=str)

        # Named (optional) arguments
        parser.add_argument(
            '-d',
            action='store_true',
        )

        # Positional arguments
        parser.add_argument('name_file', nargs='+', type=str)

        # Named (optional) arguments
        parser.add_argument(
            '-f',
            action='store_true',
        )

