from django.contrib import admin
from .models import Flavor
# Register your models here.

class FlavorsAdmin(admin.ModelAdmin):
    readonly_fields = ('created','modified')

admin.site.register(Flavor, FlavorsAdmin)