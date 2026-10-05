from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Inmueble

User = get_user_model()  # Dynamically gets your active custom user model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # Specify the fields you want to show in the signup form.
        # For example, if you added 'first_name' or custom fields:
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name', 'rut', 'tipo_usuario_defecto')
    

class ActualizarUsuarioForm(forms.ModelForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email", "first_name", "last_name", "tipo_usuario_defecto")
        labels = {
            "username": "Nombre de usuario",
            "email": "Email",
            "first_name": "Nombre",
            "last_name": "Apellido",
        }

class ActualizarInmuebleForm(forms.ModelForm):
    class Meta():
        model = Inmueble
        exclude = ["dueno"]

class CrearInmuebleForm(forms.ModelForm):
    class Meta():
        model = Inmueble
        exclude = ["dueno"]