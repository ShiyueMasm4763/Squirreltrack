from django.core.management.base import BaseCommand, CommandError
from sightings.models import Squirrel
from django.http import HttpResponse

import csv

class Command(BaseCommand):
    help = 'Export data to csv'

    def add_arguments(self, parser):
        parser.add_argument('file_path', help='filepath name')

    def handle(self, *args, **options):
        meta = Squirrel._meta
        field_names = [f.name for f in meta.fields]
        file_path = options['file_path']
        print(file_path)
        with open(file_path,'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(field_names)
            for instance in Squirrel.objects.all():
                writer.writerow([getattr(instance, field) for field in field_names])
