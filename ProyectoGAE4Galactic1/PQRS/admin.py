from django.contrib import admin
from .models import PQRS
@admin.register(PQRS)
class PQRSAdmin(admin.ModelAdmin):
    list_display = ('tipoPQRS', 'fechaPQRS', 'cliente','DescripcionPQRS','EstadoPQRS')
    #list_display_links = ('name')
    list_editable = ('EstadoPQRS',)
    search_fields = ('DescripcionPQRS',)
    list_filter = ('EstadoPQRS','fechaPQRS','tipoPQRS',)
    list_per_page = 5