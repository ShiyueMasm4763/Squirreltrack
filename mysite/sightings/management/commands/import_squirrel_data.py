from sightings.models import Squirrel
import csv
from django.core.management import BaseCommand
import datetime

class Command(BaseCommand):
    help = 'Get access to the content in the CSV file'

    def add_arguments(self, parser):
        
        parser.add_argument('path', type=str)

    def handle(self, *args, **kwargs):
        
        path = kwargs['path']
        with open(path) as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                for i in range(15,29):
                    if i!=20:
                        if row[i] == 'false' or row[i] == 'FALSE':
                            row[i] = False
                        else:
                            row[i] = True
                longitude = row[0]
                latitude = row[1]
                unique_squirrel_id = row[2]
                shift = row[4]
                date = datetime.datetime.strptime(row[5],"%m%d%Y").strftime("%Y-%m-%d")
                age = row[7]
                primary_fur_color = row[8]
                highlight_fur_color = row[9]
                combination_fur = row[10]
                color_notes = row[11]
                location = row[12]
                above_ground_sighter_measurement= row[13]
                specific_location = row[14]
                running = row[15]
                chasing = row[16]
                climbing = row[17]
                eating = row[18]
                foraging = row[19]
                other_activities = row[20]
                kuks = row[21]
                quaas = row[22]
                moans = row[23]
                tail_flags = row[24]
                tail_twitches = row[25]
                approaches = row[26]
                indifferent = row[27]
                runs_from = row[28]
                other_interactions = row[29]

                db = Squirrel(
			X = longitude, 
			Y = latitude, 
			Unique_Squirrel_ID = unique_squirrel_id, 
			Shift = shift, 
			Date = date, 
			Age = age, 
			Primary_Fur_Color = primary_fur_color,
                        Highlight_Fur_Color = highlight_fur_color,
                        Combination_Fur = combination_fur,
                        Color_Notes = color_notes,
			Location = location, 
                        Above_Ground_Sighter_Measurement = above_ground_sighter_measurement,
			Specific_Location = specific_location, 
			Running = running, 
			Chasing = chasing, 
			Climbing = climbing, 
			Eating = eating, 
			Foraging = foraging, 
			Other_Activities = other_activities, 
			Kuks = kuks, 
			Quaas = quaas, 
			Moans = moans, 
			Tail_Flags = tail_flags, 
			Tail_Twitches = tail_twitches, 
			Approaches = approaches, 
			Indifferent = indifferent, 
			Runs_From = runs_from,
                        Other_Interactions = other_interactions,
			)
                db.save() 
