from django.shortcuts import render
from .models import Producto

def index(request):
    products = Producto.objects.all()  # Obtiene todos los productos de la base de datos
    return render(request, 'index.html', {'products': products})

# Create your views here.
