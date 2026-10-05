from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm 
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.core.exceptions import PermissionDenied

from .forms import ActualizarInmuebleForm, ActualizarUsuarioForm, CustomUserCreationForm, CrearInmuebleForm
from .models import Comuna, Inmueble, Region

# Create your views here.

def index(request):
    inmuebles = Inmueble.objects.all()
    regiones = Region.objects.annotate(total_inmuebles=Count("comuna__inmueble"))
    comunas = Comuna.objects.annotate(total_inmuebles=Count("inmueble"))
    region_id = request.GET.get('region')
    comuna_id = request.GET.get('comuna')
    
    if comuna_id:
        inmuebles = inmuebles.filter(comuna_id=comuna_id)
    elif region_id:
        inmuebles = inmuebles.filter(comuna__region_id=region_id)
        comunas = comunas.filter(region_id=region_id)

    contexto = {
        "inmuebles": inmuebles, 
        "regiones": regiones, 
        "comunas": comunas,
        "region_seleccionada": region_id,  
        "comuna_seleccionada": comuna_id   
    }
    
    return render(request, 'index.html', contexto)

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('indice') 
    else:
        form = CustomUserCreationForm()
        
    return render(request, 'registration/register.html', {'form': form})


@login_required
def dashboard(request):
    inmuebles = Inmueble.objects.filter(dueno=request.user)
    return render(request, "dashboard.html", {"inmuebles":inmuebles})

@login_required
def actualizar_perfil(request):

    if request.method == "POST":
        formulario = ActualizarUsuarioForm(request.POST, instance=request.user)

        if formulario.is_valid():
            formulario.save()
            return redirect("dashboard")
    
    else:
        formulario = ActualizarUsuarioForm(instance=request.user)
        return render(request, "actualizar_perfil.html", {"form" : formulario})

def actualizar_inmueble(request, id):
    inmueble = get_object_or_404(klass=Inmueble, id=id)
    if request.method == "POST":
        form = ActualizarInmuebleForm(request.POST, instance=inmueble)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else: 
        form = ActualizarInmuebleForm(instance=inmueble)
    
    return render(request, "actualizar_inmueble.html", {"form":form, "inmueble":inmueble})

@login_required
def borrar_inmueble(request, id:int):
    inmueble = get_object_or_404(klass=Inmueble, id=id)
    if inmueble.dueno != request.user:
        raise PermissionDenied("No tienes permiso para eliminar este inmueble")
    
    if request.method == 'POST':
        inmueble.delete()
        return redirect("dashboard")
    return redirect('dashboard')

@login_required
def agregar_inmueble(request):
    if request.method == 'POST':
        form = CrearInmuebleForm(request.POST)
        if form.is_valid():
            inmueble = form.save(commit=False)
            inmueble.dueno = request.user
            inmueble.save()
            return redirect('dashboard') 
    else:
        form = CrearInmuebleForm()
        
    return render(request, 'crear_inmueble.html', {'form': form})
