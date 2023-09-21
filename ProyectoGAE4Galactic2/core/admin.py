from django.contrib import admin


from .models import TipoProducto,Producto,Marca,Venta,DetalleVenta

@admin.register(Producto)
class ProductAdmin(admin.ModelAdmin):
    fields =('nombre_producto','Descripcion_Producto','PrecioProducto','Estado_Producto','tipo_producto','marca','image')
    list_display =('__str__', 'slug',)
    list_filter = ('Estado_Producto','tipo_producto', 'marca',)


@admin.register(TipoProducto)
class TipoProductoAdmin (admin.ModelAdmin):
   
    search_fields = ('nombre_Producto',)


@admin.register(Marca)
class MarcaAdmin (admin.ModelAdmin):
    
    search_fields = ('nombre_marca',)

@admin.register(Venta)
class Admin (admin.ModelAdmin):
    fields =('Fecha_venta','total_venta','cliente')
    list_filter =('Fecha_venta',)

@admin.register(DetalleVenta)
class Admin (admin.ModelAdmin):
    fields =('PrecioVenta','Cantidad','venta','producto',)
    

