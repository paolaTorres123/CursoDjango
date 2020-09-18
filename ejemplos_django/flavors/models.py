from django.db import models
from core.models import TimeStampedModel
# Create your models here.

class Flavor(TimeStampedModel):
    title = models.CharField(max_length=200,verbose_name="Titulo")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
