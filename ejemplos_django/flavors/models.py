from django.db import models
from core.models import TimeStampedModel
# Create your models here.

class Flavor(TimeStampedModel):
    STATUS_0 = 0
    STATUS_1 = 1
    STATUS_CHOICES=(
        (STATUS_0, 'zero'),
        (STATUS_1 = 'one'),
    )
    title = models.CharField(max_length=200,verbose_name="Titulo")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    scoops_remaining = models.IntegerField(choices=STATUS_CHOICES,
        default=STATUS_0)
        
    def get_absolute_url(self):
        return reverse("flavors:detail", kwargs={"slug": self.slug})