# Generated by Django 4.2.4 on 2023-09-11 12:43

from django.db import migrations, models


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
                ('estado_cliente', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo'), ('Bloqueado', 'Bloqueado')], default='Activo', max_length=20, verbose_name='Estado del cliente')),
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
                ('estado_empleado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo'), ('Bloqueado', 'Bloqueado')], default='Activo', max_length=20, verbose_name='Estado del empleado')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'db_table': 'empleado',
                'ordering': ['nombre_empleado'],
            },
        ),
    ]
