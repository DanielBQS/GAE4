from django.shortcuts import render
from django.shortcuts import redirect


from django.contrib import messages
from django.contrib.auth import login 
from django.contrib.auth import authenticate

def index(request):
    return render(request,'index.html',  {
        #context
    })


def login_view(request):
    if request.method== 'POST':
        username= request.POST.get('correoInicio')
        password= request.POST.get('contraInicio')

        user= authenticate(username=username, password=password)
        if user:
            login(request, user)
            print("usuario autenticado")
            messages.success(request, 'Bienvenido{}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña no validos')
    
    return render(request,'users/login.html', {

    })
def HDD_view (request):
    return render(request,'Almacenamiento/HDD.html',  {
        #context
    })
def PQRSC_view (request):
    return render(request,'PQRS/PQRScliente/IndexPQRS.html',  {
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



