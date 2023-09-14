from django.contrib import admin

from .models import TipoProducto,Producto,Marca,PQRS,PQRSRespuesta,Venta

admin.site.register(Venta)
admin.site.register(PQRSRespuesta)
admin.site.register(TipoProducto)
admin.site.register(Producto)
admin.site.register(Marca)

