from django.core.management.base import BaseCommand
from sighting.models import Squirrel
import csv

class Command(BaseCommand):

    help = 'Export the data in CSV format'
    
    def handle(self,*args,**kwargs):
    
    with open('export_squirrel_data.csv',mode='w') as csvfile:
        set2 = csv.writer(csvfile,delimiter = ',')
        all_fields = [field1.name for field1 in Squirrel._meta.get_fields()]
        fieldnames = [Squirrel._meta.get_field(field2).help_text for field2 in all_fields[1:]]
        writer.writerow(fieldnames)
        for i in range(len(Squirrel.objects.all())):
            rowval = []
            for j in all_fields:
                if j == 'id':
                    continue
                rowval.append(getattr(Squirrel.objects.all()[i],j))
            writer.writerow(rowval)
    csvfile.close
