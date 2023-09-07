from django.contrib import admin
from core.models import Inventario, Producto, TipoProducto, Marca

admin.site.register(Inventario)
admin.site.register(Producto)
admin.site.register(TipoProducto)
admin.site.register(Marca)