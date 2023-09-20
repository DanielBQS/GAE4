from django.contrib import admin

from .models import TipoProducto,Producto,Marca,PQRS,PQRSRespuesta,Venta

admin.site.register(Venta)
admin.site.register(PQRSRespuesta)
admin.site.register(TipoProducto)
admin.site.register(Marca)

class ProductAdmin(admin.ModelAdmin):
    fields =('nombre_producto','Descripcion_Producto','PrecioProducto','Estado_Producto','tipo_producto','marca','image')
    list_display =('__str__', 'slug',)
admin.site.register(Producto,ProductAdmin)