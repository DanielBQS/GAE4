from import_export import resources 
from PQRS.models import PQRS,PQRSRespuesta

class PQRSResource(resources.ModelResource):
    class Meta:
        model = PQRS
        

class PQRSRespuestaResource(resources.ModelResource):
    class Meta:
        model = PQRSRespuesta
        