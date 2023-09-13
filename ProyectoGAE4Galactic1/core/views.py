from typing import Any
from django.shortcuts import render
from .models import Producto
from django.views.generic.detail import DetailView

def index(request):
    products = Producto.objects.all()  # Obtiene todos los productos de la base de datos
    return render(request, 'index.html', {'products': products})

# Create your views here.

class ProductDetailView(DetailView):
    model = Producto
    template_name ='products/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        

        print(context)
        return context