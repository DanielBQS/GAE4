from django.contrib import admin

from .models import Cliente, Empleado,TipoProducto,Producto,Marca

admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(TipoProducto)
admin.site.register(Producto)
admin.site.register(Marca)

