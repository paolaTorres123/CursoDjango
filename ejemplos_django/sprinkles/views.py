from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Sprinkle
from .utils import check_sprinkles

# Create your views here.

def sprinkle_list(request):
    """Standard list view"""
    request = check_sprinkles(request)
    return render(request,
        "sprinkles/sprinkle_list.html",
        {"sprinkles": Sprinkle.objects.all()})

def sprinkle_detail(request, pk):
    """Standard detail view"""
    request = check_sprinkles(request)
    sprinkle = get_object_or_404(Sprinkle, pk=pk)
    return render(request, "sprinkles/sprinkle_detail.html",
        {"sprinkle": sprinkle})

def sprinkle_preview(request):
    """Preview of new sprinkle, but without the
        check_sprinkles function being used.
    """
    sprinkle = Sprinkle.objects.all()
    return render(request,
        "sprinkles/sprinkle_preview.html",
        {"sprinkle": sprinkle})