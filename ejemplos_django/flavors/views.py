from django.shortcuts import render
from .models import Flavor
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils import timezone
# Create your views here.
def flavor(request):
    flavors = Flavor.objects.all()
    return render(request,"flavors/flavors.html",{'flavors':flavors})

@transaction.non_atomic_requests
def posicion_flavor_status(request,pk,status):
    flavor = get_object_or_404(Flavor,pk=pk)
    flavor.latest_status_change_attempt = timezone.now()
    flavor.save()

    with transaction.atomic():
        flavor.status = status
        flavor.latest_status_change_success = timezone.now()
        flavor.save()
        return HttpResponse('Horario')
    return HttpResponse('Sadness',status_code=400)
