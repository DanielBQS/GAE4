from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
    path('',views.index, name='index'),
    path('admin/', admin.site.urls),
    path('usuarios/login', views.login_view, name='login'),
    path('PQRS/PQRScliente', views.PQRSC_view, name='PQRScliente'),
    path('Almacenamiento/HDD', views.HDD_view, name='HDD'),
    path('Dashboard/Empleado', views.Dashboard_view, name='DashEmpleado'),
    path('Dashboard/Empleado/PQRS', views.PQRSE_view, name='PQRSempleado'),
]
