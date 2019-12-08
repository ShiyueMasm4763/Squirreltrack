from django.db import models

from django.utils.translation import gettext as _

class Squirrel(models.Model):
    X = models.FloatField(
        null=True,
        blank = True,
    ) 
    
    Y = models.FloatField(
        null=True,
        blank = True,
    )


    Unique_Squirrel_ID = models.CharField(
        max_length=20,
        null=True,
    )

    AM = 'AM'
    PM = 'PM'

    Shift = models.CharField(
        choices = (
            (AM, 'In the morning'),
            (PM, 'In the afternoon'),
        ),
        default = AM,
        max_length = 20,
        null = True,
        blank = True,
	)

    Date = models.DateField(
        null = True,
        blank = True,
    )

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    UNKNOWN = 'Unknown'
    BLANK = ''

    Age = models.CharField(
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
        blank = True,
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
        blank = True,
    )


    Combination_Fur = models.CharField(
        max_length = 100,
        null = True,
        blank = True,
    )

    Color_Notes = models.CharField(
        max_length = 100,
        null = True,
        blank = True,
    )

    AG = 'Above Ground'
    GP = 'Ground Plane'
    UNKNOWN = '?'
    BLANK = ''

    Location = models.CharField(
        choices = (
            (AG, 'Above Ground'),
            (GP, 'Ground Plane'),
            (UNKNOWN, '?'),
            (BLANK, '')
        ),
        default = BLANK,
        max_length = 20,
        null = True,
        blank = True,
    )
    TRUE = 'TRUE'
    FALSE = 'FALSE'

    Above_Ground_Sighter_Measurement = models.CharField(
        default = FALSE,
        max_length = 20,
        null = True,
        blank = True,
    )

    Specific_Location = models.CharField(
        max_length = 100,
        null = True,
        blank = True,
    )

    Running = models.CharField(
            choices=((TRUE,'true'),(FALSE,'false')),
            default=FALSE,
            max_length=10,
            null=True,
            blank = True,
    )
    Chasing = models.CharField(
            choices=((TRUE,'true'),(FALSE,'false')),
            default=FALSE,
            max_length=10,
            null=True,
            blank = True,
    )
    Climbing = models.CharField(
            choices=((TRUE,'true'),(FALSE,'false')),
            default=FALSE,
            max_length=10,
            null=True,
            blank = True,
    )
    Eating = models.CharField(
            choices=((TRUE,'true'),(FALSE,'false')),
            default=FALSE,
            max_length=10,
            null=True,
            blank = True,
    )
    Foraging = models.CharField(
            choices=((TRUE,'true'),(FALSE,'false')),
            default=FALSE,
            max_length=10,
            null=True,
            blank = True,
    )

    Other_Activities = models.CharField(
        max_length = 100,
        null = True,
        blank = True,
    )

    Kuks = models.CharField(
            choices=((TRUE,'true'),(FALSE,'false')),
            default=FALSE,
            max_length=10,
            null=True,
            blank = True,
    )
    Quaas = models.CharField(
            choices=((TRUE,'true'),(FALSE,'false')),
            default=FALSE,
            max_length=10,
            null=True,
            blank = True,
    )
    Moans = models.CharField(
            choices=((TRUE,'true'),(FALSE,'false')),
            default=FALSE,
            max_length=10,
            null=True,
            blank = True,
    )
    Tail_Flags = models.CharField(
            choices=((TRUE,'true'),(FALSE,'false')),
            default=FALSE,
            max_length=10,
            null=True,
            blank = True,
    )
    Tail_Twitches = models.CharField(
            choices=((TRUE,'true'),(FALSE,'false')),
            default=FALSE,
            max_length=10,
            null=True,
            blank = True,
    )
    Approaches = models.CharField(
            choices=((TRUE,'true'),(FALSE,'false')),
            default=FALSE,
            max_length=10,
            null=True,
            blank = True,
    )
    Indifferent = models.CharField(
            choices=((TRUE,'true'),(FALSE,'false')),
            default=FALSE,
            max_length=10,
            null=True,
            blank = True,
    )
    Runs_From = models.CharField(
            choices=((TRUE,'true'),(FALSE,'false')),
            default=FALSE,
            max_length=10,
            null=True,
            blank = True,
    )

    Other_Interactions = models.CharField(
        max_length = 50,
        null = True,
        blank = True,
    )
