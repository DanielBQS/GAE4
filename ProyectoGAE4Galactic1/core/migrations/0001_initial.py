# Generated by Django 4.2.4 on 2023-08-28 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cliente', models.CharField(max_length=60, verbose_name='Nombre del cliente')),
                ('Fecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('CorreoElectronicoC', models.CharField(max_length=40, verbose_name='Correo electrónico')),
                ('DiereccionC', models.CharField(max_length=40, verbose_name='Dirección')),
                ('NombreUsuario', models.CharField(max_length=30, verbose_name='Nombre de usuario')),
                ('Contraseña', models.CharField(max_length=20, verbose_name='Contraseña')),
                ('Estado_cliente', models.CharField(max_length=20, verbose_name='Estado del cliente')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'db_table': 'cliente',
                'ordering': ['nombre_cliente'],
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empleado', models.CharField(max_length=60, verbose_name='Nombre del empleado')),
                ('CorreoElectronicoE', models.CharField(max_length=40, verbose_name='Correo electrónico')),
                ('DiereccionE', models.CharField(max_length=40, verbose_name='Dirección')),
                ('Num_identificacion', models.BigIntegerField(verbose_name='Número de identificación')),
                ('NombreUsuarioE', models.CharField(max_length=30, verbose_name='Nombre de usuario')),
                ('ContraseñaE', models.CharField(max_length=20, verbose_name='Contraseña')),
                ('Estado_Empleado', models.CharField(max_length=20, verbose_name='Estado del empleado')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'db_table': 'empleado',
                'ordering': ['nombre_empleado'],
            },
        ),
        migrations.CreateModel(
            name='PQRS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoPQRS', models.CharField(max_length=20, verbose_name='Tipo de PQRS')),
                ('fechaPQRS', models.DateField(verbose_name='Fecha de PQRS')),
                ('EstadoPQRS', models.CharField(max_length=30, verbose_name='Estado de PQRS')),
                ('DescripcionPQRS', models.CharField(max_length=100, verbose_name='Descripción de PQRS')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente', verbose_name='Cliente')),
            ],
            options={
                'verbose_name': 'PQRS',
                'verbose_name_plural': 'PQRSs',
                'db_table': 'pqrs',
                'ordering': ['tipoPQRS'],
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_proveedor', models.CharField(max_length=60, verbose_name='Nombre del proveedor')),
                ('TelefonoProveedor', models.BigIntegerField(verbose_name='Teléfono del proveedor')),
                ('CorreoElectronicoP', models.CharField(max_length=40, verbose_name='Correo electrónico')),
                ('DiereccionP', models.CharField(max_length=40, verbose_name='Dirección')),
                ('Estado_proveedor', models.CharField(max_length=20, verbose_name='Estado del proveedor')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
                'db_table': 'proveedor',
                'ordering': ['nombre_proveedor'],
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_rol', models.CharField(max_length=20, verbose_name='Rol')),
            ],
            options={
                'verbose_name': 'Rol',
                'verbose_name_plural': 'Roles',
                'db_table': 'rol',
                'ordering': ['nombre_rol'],
            },
        ),
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_Producto', models.CharField(max_length=20, verbose_name='Nombre del producto')),
            ],
            options={
                'verbose_name': 'Tipo de Producto',
                'verbose_name_plural': 'Tipos de Productos',
                'db_table': 'tipo_producto',
                'ordering': ['nombre_Producto'],
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_transaccion', models.CharField(max_length=20, verbose_name='ID de transacción')),
                ('Fecha_venta', models.DateTimeField(verbose_name='Fecha de venta')),
                ('estado_venta', models.CharField(max_length=20, verbose_name='Estado de venta')),
                ('email', models.CharField(max_length=40, verbose_name='Correo electrónico')),
                ('total_venta', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total de venta')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente', verbose_name='Cliente de la venta')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
                'db_table': 'venta',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=60, verbose_name='Nombre del producto')),
                ('Descripcion_Producto', models.CharField(max_length=60, verbose_name='Descripción del producto')),
                ('PrecioProducto', models.BigIntegerField(verbose_name='Precio del producto')),
                ('MarcaProducto', models.CharField(max_length=20, verbose_name='Marca del producto')),
                ('Estado_Producto', models.CharField(max_length=20, verbose_name='Estado del producto')),
                ('tipo_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipoproducto', verbose_name='Tipo de producto')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'producto',
                'ordering': ['nombre_producto'],
            },
        ),
        migrations.CreateModel(
            name='PQRSRespuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta', models.CharField(max_length=100, verbose_name='Respuesta')),
                ('estado', models.CharField(max_length=20, verbose_name='Estado de respuesta')),
                ('fecha_respuesta', models.DateField(verbose_name='Fecha de respuesta')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.empleado', verbose_name='Empleado')),
                ('pqrs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pqrs', verbose_name='PQRS')),
            ],
            options={
                'verbose_name': 'Respuesta de PQRS',
                'verbose_name_plural': 'Respuestas de PQRS',
                'db_table': 'pqrs_respuesta',
                'ordering': ['respuesta'],
            },
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cantidad_productos', models.IntegerField(verbose_name='Cantidad de productos')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto', verbose_name='Producto')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.proveedor', verbose_name='Proveedor del inventario')),
            ],
            options={
                'verbose_name': 'Inventario',
                'verbose_name_plural': 'Inventarios',
                'db_table': 'inventario',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='empleado',
            name='rol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.rol', verbose_name='Rol'),
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NomVenta', models.CharField(max_length=30, verbose_name='Nombre de venta')),
                ('PrecioVenta', models.BigIntegerField(verbose_name='Precio de venta')),
                ('Cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto', verbose_name='Producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.venta', verbose_name='Venta')),
            ],
            options={
                'verbose_name': 'Detalle de Venta',
                'verbose_name_plural': 'Detalles de Venta',
                'db_table': 'detalle_venta',
                'ordering': ['id'],
            },
        ),
    ]
