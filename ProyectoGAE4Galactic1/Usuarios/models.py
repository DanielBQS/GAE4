from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save

class User(AbstractUser):
    # Campos personalizados para almacenar información adicional
    fecha_nacimiento = models.DateField(null=True, blank=True)
    direccion = models.CharField(max_length=50, blank=True)
    # Agrega más campos según tus necesidades

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
class Cliente(models.Model):
   
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    direccion = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'cliente'
        ordering = ['id']    
# Modelo de Empleado
class Empleado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
# Señal que se ejecuta después de que se guarda un usuario
@receiver(post_save, sender=User)
def crear_empleado(sender, instance, created, **kwargs):
    if created and instance.groups.filter(name='Empleados').exists():
        Empleado.objects.create(user=instance)

@receiver(post_save, sender=User)
def guardar_empleado(sender, instance, **kwargs):
    if instance.groups.filter(name='Empleados').exists():
        instance.empleado.save()
        
class Customer(User):
    class Meta:
        proxy = True

    def get_products(self):
        return []