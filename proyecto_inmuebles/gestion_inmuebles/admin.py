from django.contrib import admin
from .models import Region, Comuna, Usuario, Inmueble, Solicitud, TipoInmueble
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Region)
#admin.site.register(Comuna)
#admin.site.register(Usuario)
#admin.site.register(Inmueble)
admin.site.register(Solicitud)
admin.site.register(TipoInmueble)

@admin.register(Inmueble)
class InmuebleAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'precio_mensual')
    search_fields = ('nombre', 'direccion')
    list_filter = ('precio_mensual', 'comuna__region','tipo_inmueble')
    readonly_fields = ('fecha_creacion', 'ultima_modificacion')

@admin.register(Comuna)
class Comuna(admin.ModelAdmin):
    list_display = ('nombre', 'region')
    search_fields = ('nombre', 'region')
    list_filter = ('region',)

@admin.register(Usuario)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'rut')
    fieldsets = UserAdmin.fieldsets + (
        ('Campos personalizados', {
            'fields': ('rut', 'direccion', 'telefono', 'tipo_usuario_defecto'),
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Campos personalizados', {
            'fields': ('rut', 'direccion', 'telefono', 'tipo_usuario_defecto'),
        }),
    )

