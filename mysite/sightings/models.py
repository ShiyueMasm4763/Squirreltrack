from django.db import models

from django.utils.translation import gettext as _

class Squirrel(models.Model):
 
    X = models.DecimalField(
        help_text=('longitude'),
        max_digits=20,
        decimal_places=17,
        null=True,
    )

    Y = models.DecimalField(
        help_text=_('latitude'),
        max_digits=20,
        decimal_places=17,
        null=True,
    )

    Unique_Squirrel_ID = models.CharField(
        help_text=_('Unique_Squirrel_ID'),
        max_length=20,
        null=True,
    )

    AM = 'AM'
    PM = 'PM'

    Hectare = models.CharField(
        help_text=_('Hectare'),
        max_length=20
    )

    Shift = models.Charfield(
        help_text=_('Morning or Afternoon Shift'),
        choices = (
            (AM, 'In the morning'),
            (PM, 'In the afternoon'),
        ),
        default = AM,
        max_length = 20,
        null = True,

    Date = models.DateField(
        help_text = _('Date encountered'),
        null = True,
    )

    Hectare_Squirrel_Number = models.PositiveIntegerField(
        help_text=_("Squirrel's Number"),
        null=True,
    )

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    UNKNOWN = 'Unknown'

    Age = models.CharField(
        help_text=_('Age')
        choices = (
            (ADULT, 'Adult'),
            (JUVENILE, 'Juvenile'),
            (UNKNOWN, '     '),
        ),
        default = UNKNOWN,
        max_length = 20,
        null = True,
    )

    GRAY = 'Gray'
    BLACK = 'Black'
    CINNAMMON = 'Cinnammon'
    UNKNOWN = '     '

    Primary_Fur_Color = models.CharField(
        help_text=_('Primary Fur Color'),
        choices = (
            (GRAY, 'Gray'),
            (BLACK, 'Black'),
            (CINNAMMON, 'Cinnammon'),
            (UNKNOWN, '     '),
        ),

        default = UNKNOWN,
        max_length = 20,
        null = True,
    )

    G = 'Gray'
    B = 'Black'
    C = 'Cinnammon'
    W = 'White'
    BC = 'Black, Cinnammon'
    BW = 'Black, White'
    BCW = 'Black, Cinnammon, White'
    CW = 'Cinnammon, White'
    GB = 'Gray, Black'
    BW = 'Black, White'
    GW = 'Gray, White'
    UNKNOWN = '     '

    Highlight_Fur_Color = models.CharField(

        help_text=_('Highlight Fur Color'),
        choices = (
            (G, 'Gray'),
            (B, 'Black'),
            (C, 'Cinnammon'),
            (W, 'White'),
            (BC, 'Black, Cinnammon'),
            (BW, 'Black, White'),
            (BCW, 'Black, Cinnammon, White'),
            (CW, 'Cinammon, White'),
            (GB, 'Gray, Black'),
            (BW, 'Black, White'),
            (GW, 'Gray, White'),
            (UNKNOWN, '     '),
        ),
        default = UNKNOWN,
        max_length = 20,
        null=True,
    )


    Combination_Fur = models.CharField(

        help_text = _('Combination Fur  Color'),
        max_length = 20,
        null = True,
    )

    Color_Notes = models.CharField(
        help_text = _('Color Notes'),
        max_length = 100,
        null = True,
    )

    AG = 'Above Ground'
    GP = 'Ground Plane'
    UNKNOWN = '     '

    Location = models.CharField(

        help_text = _('Location'),

        choices = (
            (AG, 'Above Ground'),
            (GP, 'Ground Plane'),
            (UNKNOWN, '     '),
        ),

        default = UNKNOWN,
        max_length = 20,
        null = True
    )

    TRUE = 'TRUE'
    FALSE = 'FALSE'

    Above_Ground_Sighter_Measurement = models.CharField(

        help_text = _('Above Ground Sighter Measurement'),
        default = FALSE,
        max_length = 20,
        null = True,
    )

     Specific_Location = models.CharField(
        help_text = _('Specific Location'),
        max_length = 20,
        null = True,
    )

    Running = models.CharField(choices=((TRUE,'true'),(FALSE,'false')),default=FALSE,max_length=5,null=True)
    Chasing = models.CharField(choices=((TRUE,'true'),(FALSE,'false')),default=FALSE,max_length=5,null=True)
    Climbing = models.CharField(choices=((TRUE,'true'),(FALSE,'false')),default=FALSE,max_length=5,null=True)
    Eating = models.CharField(choices=((TRUE,'true'),(FALSE,'false')),default=FALSE,max_length=5,null=True)
    Foraging = models.CharField(choices=((TRUE,'true'),(FALSE,'false')),default=FALSE,max_length=5,null=True)

    Other_Activities = models.CharField(

        help_text = _('Other Activities'),
        max_length = 100,
        null = True,
    )

    Kuks = models.CharField(choices=((TRUE,'true'),(FALSE,'false')),default=FALSE,max_length=5,null=True)
    Quaas = models.CharField(choices=((TRUE,'true'),(FALSE,'false')),default=FALSE,max_length=5,null=True)
    Moans = models.CharField(choices=((TRUE,'true'),(FALSE,'false')),default=FALSE,max_length=5,null=True)
    Tail_Flags = models.CharField(choices=((TRUE,'true'),(FALSE,'false')),default=FALSE,max_length=5,null=True)
    Tail_Twitches = models.CharField(choices=((TRUE,'true'),(FALSE,'false')),default=FALSE,max_length=5,null=True)
    Approaches = models.CharField(choices=((TRUE,'true'),(FALSE,'false')),default=FALSE,max_length=5,null=True)
    Indifferent = models.CharField(choices=((TRUE,'true'),(FALSE,'false')),default=FALSE,max_length=5,null=True)
    Runs_From = models.CharField(choices=((TRUE,'true'),(FALSE,'false')),default=FALSE,max_length=5,null=True)

    Other_Interactions = models.CharField(

        help_text = _('Other Interactions'),
        max_length = 50,
        null = True,
    )











