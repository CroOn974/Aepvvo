from .models import *

# API
from rest_framework import generics
from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializer import *


##
# Récupère toutes les marques de voiture
# EndPoint -> http://localhost:8000/api/manufacturer/
#
class ManufacturerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

##
# Récupère toutes les modeles selons la marque données
# EndPoint -> http://localhost:8000/api/manufacturer/<str:manufacturer>
#
class ModelViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ModelSerializer
    queryset = Model.objects.none()

    def list(self, request, *args, **kwargs):
        # Récupérer le nom de la marque dans les paramètres de l'URL
        manufacturer_libele = kwargs.get('manufacturer_libele', '')

        # Vérifier si la marque existe
        try:
            manufacturer = Manufacturer.objects.get(manufacturer_libele=manufacturer_libele)
        except Manufacturer.DoesNotExist:
            return Response({'detail': f"La marque '{manufacturer_libele}' n'existe pas."}, status=status.HTTP_404_NOT_FOUND)
        
        # Récupérer les modèles de la marque
        models = Model.objects.filter(manufacturer_libele=manufacturer)

        # Serializer les modèles et retourner la réponse
        serializer = self.serializer_class(models, many=True)
        return Response(serializer.data)
    

##
# Récupère toutes les cathegorie de voiture
# EndPoint -> http://localhost:8000/api/category/
#
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


##
# Récupère toutes nombre de cylindres
# EndPoint -> http://localhost:8000/api/cylinders/
#
class CylindersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cylinders.objects.all()
    serializer_class = CylindersSerializer


##
# Récupère les differents type de fuel
# EndPoint -> http://localhost:8000/api/fuel/
#
class FuelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Fuel.objects.all()
    serializer_class = FuelsSerializer


##
# Récupère les differents type de roue motrice
# EndPoint -> http://localhost:8000/api/drivewheels/
#
class DrivewheelsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Drivewheels.objects.all()
    serializer_class = DrivewheelsSerializer


##
# Récupère les differents type de boite de vitesse
# EndPoint -> http://localhost:8000/api/gearbox/
#
class GearboxViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Gearbox.objects.all()
    serializer_class = GearboxSerializer


##
# Récupère les differents nombre de portes
# EndPoint -> http://localhost:8000/api/door/
#
class DoorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Door.objects.all()
    serializer_class = DoorSerializer


##
# Récupère les information sur la voiture du client et retourne une prédiction
#
#
class ExtimationViewSet(viewsets.ViewSet):

    def list(self, request):
        param1 = request.query_params.get('param1')
        param2 = request.query_params.get('param2')
        param3 = request.query_params.get('param3')

        # Do something with the parameters
        result = param1 + param2 + param3

        # Return a response with the result
        return Response({'result': result})