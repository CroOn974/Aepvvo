from api.models import Category, Cylinders, Door ,Drivewheels, Fuel, Gearbox, Manufacturer, Model
import pandas as pd
import sklearn
import pickle
import joblib
# API
from rest_framework import generics
from rest_framework import viewsets, status
from rest_framework.response import Response

from api.serializer import CategorySerializer, CylindersSerializer, DoorSerializer, DrivewheelsSerializer, FuelsSerializer, GearboxSerializer, ManufacturerSerializer, ModelSerializer, PredictSerializer

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder

import os
from django.conf import settings


##
# Récupère toutes les marques de voiture
# EndPoint -> http://localhost:8000/api/manufacturer/
#
class ManufacturerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

##
# Récupère toutes les modeles selons la marque données
# EndPoint -> http://localhost:8000/api/model/<str:manufacturer_libele>/
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
class PredictViewSet(viewsets.ViewSet):
    
    def create(self, request, *args, **kwargs):
        # Récupérer les données validées
        df = pd.DataFrame(request.data, index=[0])

        # Renommer les colonnes pour correspondre aux noms du modèle entraîné
        df.rename(columns={"manufacturer": "Manufacturer", 
                           "model": "Model",
                           "year": "Prod. year",
                           "category": "Category",
                           "fuelType": "Fuel type",
                           "mileage": "Mileage",
                           "gearBox": "Gear box type",
                           "engine": "Engine volume",
                           "leather": "Leather interior",
                           "airbag": "Airbags",
                           "levy": "Levy",
                           "cylinders": "Cylinders",
                           "driveWheels": "Drive wheels",
                           "turbo": "Turbo",
                           },inplace = True)
        

        # Charger le modèle entraîné
        model = joblib.load('api\model_predict\modele_regression_linaire.pkl')

        # Effectuer la prédiction
        predicted_prices = model.predict(df)

        # Renvoyer la prédiction
        response_data = {'predicted_prices': predicted_prices.tolist()}

        return Response(response_data)


