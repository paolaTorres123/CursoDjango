from django.views.generic import ListView
from .models import Flavor
from core.views import TitleSearchMixin


class FlavorListView(TitleSearchMixin, ListView):
    model = Flavor