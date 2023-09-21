from typing import Any
from django import forms
#from django.contrib.auth.models import User
from .models import User,Cliente
#from core.models import Cliente
from django.contrib.auth.models import Group

class RegisterForm(forms.Form):
    username= forms.CharField(label= 'Nombre de usuario',required=True,
                              min_length=4, max_length=50)
    firstname= forms.CharField (label='Nombres', required=True,
                                min_length=4, max_length=50)
    lastname= forms.CharField (label='Apellidos', required=True,
                                min_length=4, max_length=50)
    fechaNacimiento= forms.DateField (label='Fecha de nacimiento', required=True,
                                      widget= forms.PasswordInput(attrs={
                                  'type':'date'
                              }))
    
    email= forms.EmailField(label= 'Correo Electronico', required=True,
                            widget=forms.EmailInput(attrs={
                                'placeholder':'Example@gmail.com'
                            }))
    direction=forms.CharField (label='Direccion', required=True,
                                min_length=4, max_length=50)
    
    password= forms.CharField(label= 'Contraseña',required=True, 
                              widget= forms.PasswordInput(attrs={
                                  'type':'password'
                              }))
    password2= forms.CharField(label= 'Confirmar Contraseña',required=True, 
                              widget= forms.PasswordInput(attrs={
                                  'type':'password'
                              }))

    def clean_username(self):
        username =self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El nombre de usuario se encuentra en uso')
        return username
    
    def clean_email(self):
        email =self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo ya se encuentra en uso')
        return email
    
    def clean(self):
        cleaned_data= super().clean()
        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2','La contraseña no coincide')

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data.get('username'),
            password=self.cleaned_data.get('password'),
            first_name=self.cleaned_data.get('firstname'),
            last_name=self.cleaned_data.get('lastname'),
            email=self.cleaned_data.get('email')
        )

        # Agrega los datos adicionales al usuario personalizado
        user.fecha_nacimiento = self.cleaned_data.get('fechaNacimiento')  # Corregido aquí
        user.direccion = self.cleaned_data.get('direction')  # Corregido aquí

        user.save()

        # Crea un objeto Cliente y establece la relación con el usuario personalizado
        Cliente.objects.create(user=user)
          # Asigna el usuario al grupo "Clientes"
        grupo_clientes, _ = Group.objects.get_or_create(name='Clientes')
        grupo_clientes.user_set.add(user)
        return user










