from django.db import models
from Usuarios.models import Cliente

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