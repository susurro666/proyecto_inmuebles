from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='indice'),
    path('cuenta/', include('django.contrib.auth.urls')),
    path('cuenta/registro/', views.register_view, name='registro'),
    path("dashboard/", views.dashboard, name='dashboard'),
    path("crear_inmueble/", views.agregar_inmueble, name="crear_inmueble"),
    path("actualizar_perfil/", views.actualizar_perfil, name="actualizar_perfil"),
    path("inmueble/<int:id>/actualizar", views.actualizar_inmueble, name="actualizar_inmueble"),
    path('inmueble/<int:id>/borrar', views.borrar_inmueble, name='borrar_inmueble')
]