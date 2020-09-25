from django.shortcuts import render, redirect
from .models import Contacto,Domicilio,Alumno,Escuela
from .forms import ContactoForm,DomicilioForm,AlumnoForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator


class ListaEscuelas(ListView):
    model = Escuela
    paginate_by = 3

@permission_required('escuela.view_escuela')
def filtrarNombres(request):
    escuela = Escuela.objects.all()
    centro_educativo = ''
    if request.POST.get('centro_educativo'):
        centro_atencion = str(request.POST.get('centro_educativo'))
        escuela = escuela.filter(centro_educativo__gte=centro_educativo)

    return render(request, "escuela/escuela_list.html",{'escuela':escuela,'centro_educativo':centro_educativo})