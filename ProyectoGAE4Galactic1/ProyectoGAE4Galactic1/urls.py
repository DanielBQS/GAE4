from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from. import views

urlpatterns = [
    path('',views.index, name='index'),
    path('admin/', admin.site.urls),
#login/register
    path('usuarios/login', views.login_view, name='login'),
    path('usuarios/logout', views.logout_view, name='logout'),
    path('usuarios/register', views.register_view, name='register'),
#PQRS
    path('PQRS', views.PQRSC_view, name='PQRScliente'),
    path('PQRS/PQRSConsulta', views.PQRSConsultar_view, name='PQRSConsulta'),
    path('PQRS/PQRSActualizar/<int:pk>/', views.PQRSActualizar_view, name='PQRSActualizar'),
#almacenamiento
    path('Almacenamiento/HDD', views.HDD_view, name='HDD'),
    path('Almacenamiento/NVME', views.NVME_view, name='NVME'),
    path('Almacenamiento/SSD', views.SSD_view, name='SSD'),
    path('Almacenamiento/USB', views.USB_view, name='USB'),
#perifericos
    path('Perifericos/Mouse', views.Mouse_view, name='Mouse'),
    path('Perifericos/Teclado', views.Teclado_view, name='Teclado'),
    path('Perifericos/Audifonos', views.Audifonos_view, name='Audifonos'),
    path('Perifericos/Parlantes', views.Parlantes_view, name='Parlantes'),
#Torres
    path('Torres/Board', views.Board_view, name='Board'),
    path('Torres/Chasis', views.Chasis_view, name='Chasis'),
    path('Torres/Fuentes', views.Fuentes_view, name='Fuentes'),
    path('Torres/Graficas', views.Graficas_view, name='Graficas'),
    path('Torres/Procesador', views.Procesador_view, name='Procesador'),
    path('Torres/Ram', views.Ram_view, name='Ram'),
    path('Torres/Refrigeracion', views.Refrigeracion_view, name='Refrigeracion'),
#Monitores
    path('Monitores/Monitores', views.Monitores_view, name='Monitores'),
#Portatiles
    path('Portatiles/Portatiles', views.Portatiles_view, name='Portatiles'),


    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    
    