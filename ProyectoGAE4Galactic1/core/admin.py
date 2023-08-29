from django.contrib import admin
from .models import Cliente, Proveedor, Rol, TipoProducto, Empleado, PQRS, PQRSRespuesta, Producto, Inventario, Venta, DetalleVenta

# Registrar los modelos en el panel de administración
admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Rol)
admin.site.register(TipoProducto)
admin.site.register(Empleado)
admin.site.register(PQRS)
admin.site.register(PQRSRespuesta)
admin.site.register(Producto)
admin.site.register(Inventario)
admin.site.register(Venta)
admin.site.register(DetalleVenta)