from django.core.management.base import BaseCommand, CommandParser
from pathlib import Path
import os
import csv

from reviews.models import Category

class Command(BaseCommand):

    def  handle(self, *args, **options):
        print(options)
        dr = options.get('name_dir')
        fl = options.get('name_file')
        md =  options.get('model')
        path_to_file = ''

        if dr:
            for path, dirname, _ in os.walk(Path.cwd()):
                if dr in dirname:
                    path_to_file = Path(path) / dr
                    break

        if os.path.exists(path_to_file):
            for file in os.listdir(path_to_file):
                if file == fl:
                    with open(Path(path_to_file) / fl, encoding='utf-8') as file:
                        example_dict = csv.DictReader(file)
                        for i in example_dict:
                            try:
                                Category.objects.create(**i)
                            except:
                                pass                        
                    print('finish')
                    break
        
        

    def add_arguments(self, parser):

        # Named (optional) arguments
        parser.add_argument(
            '-d',
            action='store',
            dest='name_dir',
        )

        # Named (optional) arguments
        parser.add_argument(
            '-f',
            action='store',
            dest='name_file'
        )

        parser.add_argument(
            '-m',
            action='store',
            dest='model',
        )

