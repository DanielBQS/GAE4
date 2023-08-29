from django.db import models
from datetime import datetime

class Rol(models.Model):
    nombre_rol = models.CharField(max_length=20, verbose_name='Rol')

    def __str__(self):
        return self.nombre_rol

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        db_table = 'rol'
        ordering = ['nombre_rol']

class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=60, verbose_name='Nombre del cliente')
    Fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    CorreoElectronicoC = models.CharField(max_length=40, verbose_name='Correo electrónico')
    DiereccionC = models.CharField(max_length=40, verbose_name='Dirección')
    NombreUsuario = models.CharField(max_length=30, verbose_name='Nombre de usuario')
    Contraseña = models.CharField(max_length=20, verbose_name='Contraseña')
    Estado_cliente = models.CharField(max_length=20, verbose_name='Estado del cliente')

    def __str__(self):
        return self.nombre_cliente

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'cliente'
        ordering = ['nombre_cliente']

class Empleado(models.Model):
    nombre_empleado = models.CharField(max_length=60, verbose_name='Nombre del empleado')
    CorreoElectronicoE = models.CharField(max_length=40, verbose_name='Correo electrónico')
    DiereccionE = models.CharField(max_length=40, verbose_name='Dirección')
    Num_identificacion = models.BigIntegerField(verbose_name='Número de identificación')
    NombreUsuarioE = models.CharField(max_length=30, verbose_name='Nombre de usuario')
    ContraseñaE = models.CharField(max_length=20, verbose_name='Contraseña')
    Estado_Empleado = models.CharField(max_length=20, verbose_name='Estado del empleado')
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, verbose_name='Rol')

    def __str__(self):
        return self.nombre_empleado

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering = ['nombre_empleado']

class PQRS(models.Model):
    tipoPQRS = models.CharField(max_length=20, verbose_name='Tipo de PQRS')
    fechaPQRS = models.DateField(verbose_name='Fecha de PQRS')
    EstadoPQRS = models.CharField(max_length=30, verbose_name='Estado de PQRS')
    DescripcionPQRS = models.CharField(max_length=100, verbose_name='Descripción de PQRS')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Cliente')

    def __str__(self):
        return self.tipoPQRS

    class Meta:
        verbose_name = 'PQRS'
        verbose_name_plural = 'PQRSs'
        db_table = 'pqrs'
        ordering = ['tipoPQRS']

class PQRSRespuesta(models.Model):
    respuesta = models.CharField(max_length=100, verbose_name='Respuesta')
    estado = models.CharField(max_length=20, verbose_name='Estado de respuesta')
    fecha_respuesta = models.DateField(verbose_name='Fecha de respuesta')
    pqrs = models.ForeignKey(PQRS, on_delete=models.CASCADE, verbose_name='PQRS')
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, verbose_name='Empleado')

    def __str__(self):
        return self.respuesta

    class Meta:
        verbose_name = 'Respuesta de PQRS'
        verbose_name_plural = 'Respuestas de PQRS'
        db_table = 'pqrs_respuesta'
        ordering = ['respuesta']

class Proveedor(models.Model):
    nombre_proveedor = models.CharField(max_length=60, verbose_name='Nombre del proveedor')
    TelefonoProveedor = models.BigIntegerField(verbose_name='Teléfono del proveedor')
    CorreoElectronicoP = models.CharField(max_length=40, verbose_name='Correo electrónico')
    DiereccionP = models.CharField(max_length=40, verbose_name='Dirección')
    Estado_proveedor = models.CharField(max_length=20, verbose_name='Estado del proveedor')

    def __str__(self):
        return self.nombre_proveedor

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        db_table = 'proveedor'
        ordering = ['nombre_proveedor']

class TipoProducto(models.Model):
    nombre_Producto = models.CharField(max_length=20, verbose_name='Nombre del producto')

    def __str__(self):
        return self.nombre_Producto

    class Meta:
        verbose_name = 'Tipo de Producto'
        verbose_name_plural = 'Tipos de Productos'
        db_table = 'tipo_producto'
        ordering = ['nombre_Producto']

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=60, verbose_name='Nombre del producto')
    Descripcion_Producto = models.CharField(max_length=60, verbose_name='Descripción del producto')
    PrecioProducto = models.BigIntegerField(verbose_name='Precio del producto')
    MarcaProducto = models.CharField(max_length=20, verbose_name='Marca del producto')
    Estado_Producto = models.CharField(max_length=20, verbose_name='Estado del producto')
    tipo_producto = models.ForeignKey(TipoProducto, on_delete=models.CASCADE, verbose_name='Tipo de producto')

    def __str__(self):
        return self.nombre_producto

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'producto'
        ordering = ['nombre_producto']

class Inventario(models.Model):
    Cantidad_productos = models.IntegerField(verbose_name='Cantidad de productos')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name='Producto')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, verbose_name='Proveedor del inventario')
    def __str__(self):
        return f'Inventario {self.id}'

    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'
        db_table = 'inventario'
        ordering = ['id']

class Venta(models.Model):
    id_transaccion = models.CharField(max_length=20, verbose_name='ID de transacción')
    Fecha_venta = models.DateTimeField(verbose_name='Fecha de venta')
    estado_venta = models.CharField(max_length=20, verbose_name='Estado de venta')
    email = models.CharField(max_length=40, verbose_name='Correo electrónico')
    total_venta = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Total de venta')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Cliente de la venta')
    def __str__(self):
        return f'Venta {self.id}'

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        db_table = 'venta'
        ordering = ['id']

class DetalleVenta(models.Model):
    NomVenta = models.CharField(max_length=30, verbose_name='Nombre de venta')
    PrecioVenta = models.BigIntegerField(verbose_name='Precio de venta')
    Cantidad = models.IntegerField(verbose_name='Cantidad')
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, verbose_name='Venta')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name='Producto')

    def __str__(self):
        return f'DetalleVenta {self.id}'

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalles de Venta'
        db_table = 'detalle_venta'
        ordering = ['id']