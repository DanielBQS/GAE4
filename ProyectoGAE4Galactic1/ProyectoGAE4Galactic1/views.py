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
    