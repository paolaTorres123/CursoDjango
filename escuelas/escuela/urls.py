from django.urls import path
from . import views
from django.contrib.auth.decorators import permission_required




urlpatterns = [
    path('lista',views.ListaEscuelas.as_view(),
    name='lista_escuela'),
    path('filtro/',permission_required('escuela.view_escuela')
    (views.filtrarNombres),
    name='filtrar_nombres'),
]