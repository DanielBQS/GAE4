from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_list_or_404
from .models import Cart
from core.models import Producto
from .utils import get_or_create_cart
from .models import CartProducts


def cart(request):
    cart = get_or_create_cart(request)
        
    
    return render(request, 'carts/cart.html', {
        'cart': cart
    })
    
def add(request):
    cart = get_or_create_cart(request)
    producto = Producto.objects.get(pk=request.POST.get('producto_id'))
    quantity = request.POST.get('quantity', 1)
    
    cart.Productos.add(producto, through_defaults={
      'quantity': quantity
    })
    
    #cart_product = CartProducts.objects.create(cart=cart, producto=producto, quantity=quantity)
    
    return render(request, 'carts/add.html', {
        'producto': producto
    })
    
    
def remove(request):
    cart = get_or_create_cart(request)
    producto = Producto.objects.get(pk=request.POST.get('producto_id'))
    
    cart.Productos.remove(producto)
    
    return redirect('carts:cart')


