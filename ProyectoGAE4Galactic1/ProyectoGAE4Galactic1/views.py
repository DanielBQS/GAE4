from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import login 
from django.contrib.auth import logout 
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from PQRS.forms import PQRSFilterForm
from PQRS.forms import PQRSForm
#from django.contrib.auth.models import User
from Usuarios.models import User
from PQRS.models import PQRS
from core.models import Producto
from Usuarios.forms import RegisterForm
def index(request):
    
    products = Producto.objects.all().order_by('id')
    
    return render(request,'index.html',  {
        'message': 'listado de productos',
        'title': 'Producto',
        'products' : products,
    })


def login_view(request):
    if request.user.is_authenticated:
        # Si el usuario ya está autenticado, redirigir a la página principal
        return redirect('index')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, 'Bienvenido a nuestro sito {}'.format(user.username))

            if user.groups.filter(name='Clientes').exists():
                # Redirigir al cliente a la página principal
                return redirect('index')
            else:
                # Redirigir a empleados y administradores al panel de administrador
                return redirect('admin:index')  # Redirige al panel de administrador
            
        else:
            messages.error(request, 'Usuario o contraseña no válidos')

    return render(request, 'users/login.html')
def logout_view (request):
    logout(request)
    messages.success(request, 'Sesión finalizada exitosamente')
    return redirect ('login')
def register_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    form=RegisterForm(request.POST or None)
    if request.method== 'POST' and form.is_valid():
      
        user=form.save()
        if user:
            login(request, user)
            messages.success(request, 'Usuario registrado exitosamente')
            return redirect('index')
    return render(request,'users/register.html', {
        'form': form
    })

#PQRS
def PQRSC_view(request):
    if request.method == 'POST':
        # Recupera los datos del formulario
        tipo_pqrs = request.POST.get('tipo')
        fecha_pqrs = request.POST.get('fecha')
        descripcion_pqrs = request.POST.get('message')
        
        # Obtiene el cliente asociado al usuario logueado
        cliente = request.user.cliente

        # Crea una nueva instancia de PQRS con el cliente y otros datos
        pqrs = PQRS(
            tipoPQRS=tipo_pqrs,
            fechaPQRS=fecha_pqrs,
            DescripcionPQRS=descripcion_pqrs,
            cliente=cliente  # Asigna el cliente obtenido del usuario logueado
        )

        # Guarda la instancia en la base de datos
        pqrs.save()

        # Redirige a una página de éxito o a otra vista después de guardar la PQRS
        return redirect('PQRSConsulta')  # Reemplaza 'nombre_de_la_vista' con el nombre de tu vista

    # Si el método no es POST, renderiza la página inicial del formulario
    return render(request, 'PQRS/IndexPQRS.html')
@login_required
def PQRSConsultar_view(request):
    try:
        # Intenta obtener el cliente asociado al usuario logueado
        cliente = request.user.cliente

        # Inicializa el formulario de filtro con los datos enviados en la solicitud
        form = PQRSFilterForm(request.GET)

        # Verifica si el formulario es válido antes de continuar
        if form.is_valid():
            # Consulta las PQRS asociadas al cliente
            pqrs_list = PQRS.objects.filter(cliente=cliente)

            # Aplica el filtro de estado si se proporciona en el formulario
            estado_filtrado = form.cleaned_data.get('estado')
            if estado_filtrado:
                pqrs_list = pqrs_list.filter(EstadoPQRS=estado_filtrado)

            # Renderiza la plantilla con las PQRS del cliente y el formulario de filtro
            return render(request, 'PQRS/ConsultaPQRS/consultaPQRS.html', {'pqrs_list': pqrs_list, 'form': form})
    except PermissionDenied:
        # Si el usuario no tiene permisos para acceder, muestra un mensaje personalizado
        messages.error(request, "Si quieres consultar las PQRS, por favor revisa el panel de administrador.")
    
    # Si hay un error o el formulario no es válido, renderiza la plantilla con el formulario
    return render(request, 'PQRS/ConsultaPQRS/consultaPQRS.html', {'form': form})
    
def PQRSActualizar_view (request, pk):
    pqrs = get_object_or_404(PQRS, pk=pk)
    if request.method == 'POST':
        form = PQRSForm(request.POST, instance=pqrs)
        if form.is_valid():
            form.save()
            return redirect('PQRSConsulta')  # Redirige a la página de consulta de PQRS
    else:
        form = PQRSForm(instance=pqrs)
    return render(request, 'PQRS/ActualizarPQRS/actualizarPQRS.html', {'form': form})
# Vista para eliminar una PQRS
def eliminar_pqrs(request, pk):
    pqrs = get_object_or_404(PQRS, pk=pk)
    if request.method == 'POST':
        pqrs.delete()
        return redirect('PQRSConsulta')  # Redirige a la página de consulta de PQRS
#pagina
def HDD_view (request):
    return render(request,'Almacenamiento/HDD.html',  {
        #context
    })
  
def NVME_view (request):
    return render(request,'Almacenamiento/NVME.html', {
        #context
    })
    
def SSD_view (request):
    return render(request,'Almacenamiento/SSD.html', {
        #context
    })
    
def USB_view (request):
    return render(request,'Almacenamiento/USB.html', {
        #context
    })
    
def Mouse_view (request):
    return render(request,'Perifericos/Mouse.html', {
        #context
    })
    
def Teclado_view (request):
    return render(request,'Perifericos/Teclado.html', {
        #context
    })

def Audifonos_view (request):
    return render(request,'Perifericos/Audifonos.html', {
        #context
    })
    
def Parlantes_view (request):
    return render(request,'Perifericos/Parlantes.html', {
        #context
    })
    
#Torres

def Board_view (request):
    return render(request,'Torres/Board.html', {
        #context
    })
    
def Chasis_view (request):
    return render(request,'Torres/Chasis.html', {
        #context
    })
    
        
def Fuentes_view (request):
    return render(request,'Torres/Fuentes.html', {
        #context
    })
    
def Graficas_view (request):
    return render(request,'Torres/Graficas.html', {
        #context
    })
    
def Procesador_view (request):
    return render(request,'Torres/Procesador.html', {
        #context
    })
    
    
def Ram_view (request):
    return render(request,'Torres/Ram.html', {
        #context
    })

def Refrigeracion_view (request):
    return render(request,'Torres/Refrigeracion.html', {
        #context
    })


def Monitores_view (request):
    return render(request,'Monitores/Monitores.html', {
        #context
    })
    
def Portatiles_view (request):
    return render(request,'Portatiles/Portatiles.html', {
        #context
    })
    