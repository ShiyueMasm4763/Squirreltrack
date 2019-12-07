# Generated by Django 2.2.7 on 2019-12-07 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('X', models.DecimalField(decimal_places=17, help_text='longitude', max_digits=20, null=True)),
                ('Y', models.DecimalField(decimal_places=17, help_text='latitude', max_digits=20, null=True)),
                ('Unique_Squirrel_ID', models.CharField(help_text='Unique_Squirrel_ID', max_length=20, null=True)),
                ('Shift', models.CharField(choices=[('AM', 'In the morning'), ('PM', 'In the afternoon')], default='AM', help_text='Morning or Afternoon Shift', max_length=20, null=True)),
                ('Date', models.DateField(help_text='Date encountered', null=True)),
                ('Age', models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile'), ('Unknown', '?'), ('', '    ')], default='', help_text='Age', max_length=20, null=True)),
                ('Primary_Fur_Color', models.CharField(choices=[('Gray', 'Gray'), ('Black', 'Black'), ('Cinnammon', 'Cinnammon'), ('     ', '     ')], default='     ', help_text='Primary Fur Color', max_length=20, null=True)),
                ('Highlight_Fur_Color', models.CharField(choices=[('Gray', 'Gray'), ('Black', 'Black'), ('Cinnammon', 'Cinnammon'), ('White', 'White'), ('Black, Cinnammon', 'Black, Cinnammon'), ('Black, White', 'Black, White'), ('Black, Cinnammon, White', 'Black, Cinnammon, White'), ('Cinnammon, White', 'Cinammon, White'), ('Gray, Black', 'Gray, Black'), ('Black, White', 'Black, White'), ('Gray, White', 'Gray, White'), ('     ', '     ')], default='     ', help_text='Highlight Fur Color', max_length=50, null=True)),
                ('Combination_Fur', models.CharField(help_text='Combination of Primary and Highlight', max_length=100, null=True)),
                ('Color_Notes', models.CharField(help_text='Color Notes', max_length=100, null=True)),
                ('Location', models.CharField(choices=[('Above Ground', 'Above Ground'), ('Ground Plane', 'Ground Plane'), ('     ', '     ')], default='     ', help_text='Location', max_length=20, null=True)),
                ('Above_Ground_Sighter_Measurement', models.CharField(default='FALSE', help_text='Above Ground Sighter Measurement', max_length=20, null=True)),
                ('Specific_Location', models.CharField(help_text='Specific Location', max_length=100, null=True)),
                ('Running', models.CharField(choices=[('TRUE', 'true'), ('FALSE', 'false')], default='FALSE', help_text='Running', max_length=10, null=True)),
                ('Chasing', models.CharField(choices=[('TRUE', 'true'), ('FALSE', 'false')], default='FALSE', help_text='Chasing', max_length=10, null=True)),
                ('Climbing', models.CharField(choices=[('TRUE', 'true'), ('FALSE', 'false')], default='FALSE', help_text='Climbing', max_length=10, null=True)),
                ('Eating', models.CharField(choices=[('TRUE', 'true'), ('FALSE', 'false')], default='FALSE', help_text='Eating', max_length=10, null=True)),
                ('Foraging', models.CharField(choices=[('TRUE', 'true'), ('FALSE', 'false')], default='FALSE', help_text='Foraging', max_length=10, null=True)),
                ('Other_Activities', models.CharField(help_text='Other Activities', max_length=100, null=True)),
                ('Kuks', models.CharField(choices=[('TRUE', 'true'), ('FALSE', 'false')], default='FALSE', help_text='Kuks', max_length=10, null=True)),
                ('Quaas', models.CharField(choices=[('TRUE', 'true'), ('FALSE', 'false')], default='FALSE', help_text='Quaas', max_length=10, null=True)),
                ('Moans', models.CharField(choices=[('TRUE', 'true'), ('FALSE', 'false')], default='FALSE', help_text='Moans', max_length=10, null=True)),
                ('Tail_Flags', models.CharField(choices=[('TRUE', 'true'), ('FALSE', 'false')], default='FALSE', help_text='Tail_Flags', max_length=10, null=True)),
                ('Tail_Twitches', models.CharField(choices=[('TRUE', 'true'), ('FALSE', 'false')], default='FALSE', help_text='Tail_Twiches', max_length=10, null=True)),
                ('Approaches', models.CharField(choices=[('TRUE', 'true'), ('FALSE', 'false')], default='FALSE', help_text='Approaches', max_length=10, null=True)),
                ('Indifferent', models.CharField(choices=[('TRUE', 'true'), ('FALSE', 'false')], default='FALSE', help_text='Indifferent', max_length=10, null=True)),
                ('Runs_From', models.CharField(choices=[('TRUE', 'true'), ('FALSE', 'false')], default='FALSE', help_text='Runs_From', max_length=10, null=True)),
                ('Other_Interactions', models.CharField(help_text='Other Interactions', max_length=50, null=True)),
            ],
        ),
    ]