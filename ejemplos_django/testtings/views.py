from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView,DetailView,UpdateView
from .models import Tasting
# Create your views here.

class TasteListView(ListView):
    model = Tasting

class TasteDetailView(DetailView):
    model = Tasting

class TasteResultsView(TasteDetailView):
    template_name = 'tastings/results.html'

class TasteUpdateView(UpdateView):
    model = Tasting
    def get_success_url(self):
        return reverse('tastings:detail',
            kwargs={'pk': self.object.pk})