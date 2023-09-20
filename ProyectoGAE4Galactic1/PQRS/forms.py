from django import forms
from .models import PQRS

class PQRSFilterForm(forms.Form):
    ESTADOS_CHOICES = [
        ('', 'Todos'),  # Opción para mostrar todas las PQRS
        ('Pendiente', 'Pendiente'),
        ('En Proceso', 'En Proceso'),
        ('Resuelta', 'Resuelta'),
    ]

    estado = forms.ChoiceField(
        label='Filtrar por Estado',
        choices=ESTADOS_CHOICES,
        required=False  # El campo no es obligatorio
    )


    
class PQRSForm(forms.ModelForm):
    class Meta:
        model = PQRS  # Especifica el modelo con el que está relacionado este formulario
        fields = ['tipoPQRS', 'fechaPQRS', 'DescripcionPQRS']
        