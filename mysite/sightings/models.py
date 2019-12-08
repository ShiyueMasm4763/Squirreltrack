from django.db import models

from django.utils.translation import gettext as _

class Squirrel(models.Model):
    X = models.FloatField(

        help_text=_('X'),

        null=True,

    ) 
    
    Y = models.FloatField(

        help_text=_('Y'),

        null=True,

    )


    Unique_Squirrel_ID = models.CharField(
        help_text=_('Unique_Squirrel_ID'),
        max_length=20,
        null=True,
    )

    AM = 'AM'
    PM = 'PM'

    Shift = models.CharField(
        help_text=_('Morning or Afternoon Shift'),
        choices = (
            (AM, 'In the morning'),
            (PM, 'In the afternoon'),
        ),
        default = AM,
        max_length = 20,
        null = True,
	)

    Date = models.DateField(
        help_text = _('Date encountered'),
        null = True,
    )

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    UNKNOWN = 'Unknown'
    BLANK = ''

    Age = models.CharField(
        help_text=_('Age'),
        choices = (
            (ADULT, 'Adult'),
            (JUVENILE, 'Juvenile'),
            (UNKNOWN, '?'),
            (BLANK,''),
        ),
        default = BLANK,
        max_length = 20,
        null = True,
        blank=True,
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
            (BLANK, ''),
            (UNKNOWN, '?')
        ),

        default = BLANK,
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
    BLANK = ''
    UNKNOWN = '?'

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
            (UNKNOWN, '?'),
            (BLANK, '')
        ),
        default = BLANK,
        max_length = 50,
        null=True,
    )


    Combination_Fur = models.CharField(

        help_text = _('Combination of Primary and Highlight'),
        max_length = 100,
        null = True,
    )

    Color_Notes = models.CharField(
        help_text = _('Color Notes'),
        max_length = 100,
        null = True,
    )

    AG = 'Above Ground'
    GP = 'Ground Plane'
    UNKNOWN = '?'
    BLANK = ''

    Location = models.CharField(

        help_text = _('Location'),

        choices = (
            (AG, 'Above Ground'),
            (GP, 'Ground Plane'),
            (UNKNOWN, '?'),
            (BLANK, '')
        ),

        default = BLANK,
        max_length = 20,
        null = True,
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
        max_length = 100,
        null = True,
    )

    Running = models.CharField(
            help_text = _('Running'),
            choices=((TRUE,'true'),(FALSE,'false')),
            default=FALSE,
            max_length=10,
            null=True,
    )
    Chasing = models.CharField(
            help_text = _('Chasing'),
            choices=((TRUE,'true'),(FALSE,'false')),
            default=FALSE,
            max_length=10,
            null=True,
    )
    Climbing = models.CharField(
            help_text = _('Climbing'),
            choices=((TRUE,'true'),(FALSE,'false')),
            default=FALSE,
            max_length=10,
            null=True,
    )
    Eating = models.CharField(
            help_text = _('Eating'),
            choices=((TRUE,'true'),(FALSE,'false')),
            default=FALSE,
            max_length=10,
            null=True,
    )
    Foraging = models.CharField(
            help_text = _('Foraging'),
            choices=((TRUE,'true'),(FALSE,'false')),
            default=FALSE,
            max_length=10,
            null=True,
    )

    Other_Activities = models.CharField(

        help_text = _('Other Activities'),
        max_length = 100,
        null = True,
    )

    Kuks = models.CharField(
            help_text = _('Kuks'),
            choices=((TRUE,'true'),(FALSE,'false')),
            default=FALSE,
            max_length=10,
            null=True,
    )
    Quaas = models.CharField(
            help_text = _('Quaas'),
            choices=((TRUE,'true'),(FALSE,'false')),
            default=FALSE,
            max_length=10,
            null=True,
    )
    Moans = models.CharField(
            help_text = _('Moans'),
            choices=((TRUE,'true'),(FALSE,'false')),
            default=FALSE,
            max_length=10,
            null=True,
    )
    Tail_Flags = models.CharField(
            help_text = _('Tail_Flags'),
            choices=((TRUE,'true'),(FALSE,'false')),
            default=FALSE,
            max_length=10,
            null=True,
    )
    Tail_Twitches = models.CharField(
            help_text = _('Tail_Twiches'),
            choices=((TRUE,'true'),(FALSE,'false')),
            default=FALSE,
            max_length=10,
            null=True,
    )
    Approaches = models.CharField(
            help_text = _('Approaches'),
            choices=((TRUE,'true'),(FALSE,'false')),
            default=FALSE,
            max_length=10,
            null=True,
    )
    Indifferent = models.CharField(
            help_text = _('Indifferent'),
            choices=((TRUE,'true'),(FALSE,'false')),
            default=FALSE,
            max_length=10,
            null=True,
    )
    Runs_From = models.CharField(
            help_text = _('Runs_From'),
            choices=((TRUE,'true'),(FALSE,'false')),
            default=FALSE,
            max_length=10,
            null=True,
    )

    Other_Interactions = models.CharField(

        help_text = _('Other Interactions'),
        max_length = 50,
        null = True,
    )











