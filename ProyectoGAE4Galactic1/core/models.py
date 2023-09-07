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
        app_label = 'core' 

class Cliente(models.Model):
    ESTADO_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
        ('Bloqueado', 'Bloqueado'),
        # Puedes agregar más opciones aquí según tus necesidades
    ]

    nombre_cliente = models.CharField(max_length=60, verbose_name='Nombre del cliente')
    Fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    CorreoElectronicoC = models.CharField(max_length=40, verbose_name='Correo electrónico')
    DiereccionC = models.CharField(max_length=40, verbose_name='Dirección')
    NombreUsuario = models.CharField(max_length=30, verbose_name='Nombre de usuario')
    Contraseña = models.CharField(max_length=20, verbose_name='Contraseña')
    estado_cliente = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='Activo',  # Puedes establecer un valor predeterminado aquí
        verbose_name='Estado del cliente'
    )

    def __str__(self):
        return self.nombre_cliente

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'cliente'
        ordering = ['nombre_cliente']
        app_label = 'Usuarios' 

class Empleado(models.Model):
    ESTADO_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
        ('Bloqueado', 'Bloqueado'),
        # Agrega más opciones según tus necesidades
    ]

    nombre_empleado = models.CharField(max_length=60, verbose_name='Nombre del empleado')
    CorreoElectronicoE = models.CharField(max_length=40, verbose_name='Correo electrónico')
    DiereccionE = models.CharField(max_length=40, verbose_name='Dirección')
    Num_identificacion = models.BigIntegerField(verbose_name='Número de identificación')
    NombreUsuarioE = models.CharField(max_length=30, verbose_name='Nombre de usuario')
    ContraseñaE = models.CharField(max_length=20, verbose_name='Contraseña')
    estado_empleado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='Activo',
        verbose_name='Estado del empleado'
    )
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, verbose_name='Rol')

    def __str__(self):
        return self.nombre_empleado

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering = ['nombre_empleado']
        app_label = 'Usuarios' 

class PQRS(models.Model):
    # Definir las opciones para el campo tipo "select" de Tipo de PQRS
    OPCIONES_TIPO_PQRS = [
        ('Pregunta', 'Pregunta'),
        ('Queja', 'Queja'),
        ('Reclamo', 'Reclamo'),
        ('Sugerencia', 'Sugerencia'),
    ]

    # Campo CharField con choices para el Tipo de PQRS
    tipoPQRS = models.CharField(
        max_length=20,
        verbose_name='Tipo de PQRS',
        choices=OPCIONES_TIPO_PQRS,
    )

    # Definir las opciones para el campo tipo "select" de Estado de PQRS
    OPCIONES_ESTADO_PQRS = [
        ('Pendiente', 'Pendiente'),
        ('En Proceso', 'En Proceso'),
        ('Resuelta', 'Resuelta'),
    ]

    # Campo CharField con choices para el Estado de PQRS
    EstadoPQRS = models.CharField(
        max_length=20,
        verbose_name='Estado de PQRS',
        choices=OPCIONES_ESTADO_PQRS,
        default='Pendiente',  # Puedes establecer un valor predeterminado si lo deseas
    )

    # Resto de tus campos
    fechaPQRS = models.DateField(verbose_name='Fecha de PQRS')
    DescripcionPQRS = models.TextField(max_length=100, verbose_name='Descripción de PQRS')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Cliente')

    def __str__(self):
        return self.tipoPQRS

    class Meta:
        verbose_name = 'PQRS'
        verbose_name_plural = 'PQRSs'
        db_table = 'pqrs'
        ordering = ['tipoPQRS']
        app_label = 'PQRS' 

class PQRSRespuesta(models.Model):
    respuesta = models.TextField(max_length=100, verbose_name='Respuesta')
    
    # Definir las opciones para el campo "select" de Estado de respuesta de PQRS
    OPCIONES_ESTADO_RESPUESTA = [
        ('Pendiente', 'Pendiente'),
        ('En Proceso', 'En Proceso'),
        ('Resuelta', 'Resuelta'),
    ]

    estado = models.CharField(
        max_length=20,
        verbose_name='Estado de respuesta',
        choices=OPCIONES_ESTADO_RESPUESTA,  # Usar las opciones definidas arriba
    )

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
        app_label = 'PQRS' 

class Proveedor(models.Model):
    ESTADO_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
        ('Bloqueado', 'Bloqueado'),
        # Puedes agregar más opciones aquí según tus necesidades
    ]

    nombre_proveedor = models.CharField(max_length=60, verbose_name='Nombre del proveedor')
    TelefonoProveedor = models.BigIntegerField(verbose_name='Teléfono del proveedor')
    CorreoElectronicoP = models.CharField(max_length=40, verbose_name='Correo electrónico')
    DiereccionP = models.CharField(max_length=40, verbose_name='Dirección')
    estado_proveedor = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='Activo',  # Puedes establecer un valor predeterminado aquí
        verbose_name='Estado del proveedor'
    )

    def __str__(self):
        return self.nombre_proveedor

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        db_table = 'proveedor'
        ordering = ['nombre_proveedor']
        app_label = 'Proveedores' 

class TipoProducto(models.Model):
    nombre_Producto = models.CharField(max_length=20, verbose_name='Nombre del producto')

    def __str__(self):
        return self.nombre_Producto

    class Meta:
        verbose_name = 'Tipo de Producto'
        verbose_name_plural = 'Tipos de Productos'
        db_table = 'tipo_producto'
        ordering = ['nombre_Producto']
        app_label = 'Inventario' 

class Marca(models.Model):
    nombre_marca = models.CharField(max_length=20, verbose_name='Nombre de Marca')

    def __str__(self):
        return self.nombre_marca

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        db_table = 'marca'
        ordering = ['nombre_marca']
        app_label = 'Inventario' 

class Producto(models.Model):
    ESTADO_CHOICES = (
        ('Agotado', 'Agotado'),
        ('Disponible', 'Disponible'),
    )

    nombre_producto = models.CharField(max_length=60, verbose_name='Nombre del producto')
    Descripcion_Producto = models.CharField(max_length=60, verbose_name='Descripción del producto')
    PrecioProducto = models.BigIntegerField(verbose_name='Precio del producto')
    Estado_Producto = models.TextField(max_length=20, choices=ESTADO_CHOICES, verbose_name='Estado del producto')
    tipo_producto = models.ForeignKey(TipoProducto, on_delete=models.CASCADE, verbose_name='Tipo de producto')
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, verbose_name='Marca del producto')

    def __str__(self):
        return self.nombre_producto

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'producto'
        ordering = ['nombre_producto']
        app_label = 'Inventario' 

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
        app_label = 'Inventario' 

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
        app_label = 'Ventas' 

class DetalleVenta(models.Model):
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
        app_label = 'Ventas' 