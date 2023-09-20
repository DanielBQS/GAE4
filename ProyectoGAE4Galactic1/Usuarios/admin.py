from .models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cliente
from .models import Empleado

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('get_first_name', 'get_last_name', 'get_email', 'get_fecha_nacimiento', 'get_direccion')
    list_select_related = ('user',)

    def get_first_name(self, instance):
        return instance.user.first_name

    def get_last_name(self, instance):
        return instance.user.last_name

    def get_email(self, instance):
        return instance.user.email

    def get_fecha_nacimiento(self, instance):
        return instance.user.fecha_nacimiento

    def get_direccion(self, instance):
        return instance.user.direccion

    get_first_name.short_description = 'Nombres'
    get_last_name.short_description = 'Apellidos'
    get_email.short_description = 'Correo Electrónico'
    get_fecha_nacimiento.short_description = 'Fecha de Nacimiento'
    get_direccion.short_description = 'Dirección'

admin.site.register(User,UserAdmin)

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('user',)  # Personaliza esto según tus necesidades

