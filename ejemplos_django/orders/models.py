from django.db import models

# Create your models here.

class IceCreamOrder(models.Model):
    FLAVOR_CHOCOLATE = 'ch'
    FLAVOR_VANILLA = 'vn'
    FLAVOR_STRAWBERRY = 'st'
    FLAVOR_CHUNKY_MUNKY = 'cm'

    FLAVOR_CHOICES = (
        (FLAVOR_CHOCOLATE, 'Chocolate'),
        (FLAVOR_VANILLA, 'Vanilla'),
        (FLAVOR_STRAWBERRY, 'Strawberry'),
        (FLAVOR_CHUNKY_MUNKY, 'Chunky Munky')
    )
    flavor = models.CharField(
        max_length=2,
        choices=FLAVOR_CHOICES
    )

