from api.models import Category, Cylinders, Door ,Drivewheels, Fuel, Gearbox, Manufacturer, Model
import pandas as pd
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
        
                
        file = 'api\model_predict\model.pkl'
        # Charger le modèle à partir du fichier
        with open(file, 'rb') as f:
            model = pickle.load(f)

        model_path = os.path.join(settings.BASE_DIR, 'api', 'model_predict')
        ct = joblib.load(model_path+'/full_pipeline.pkl')
        # file2 = 'api\model_predict\full_pipeline.pkl'

        # with open(file2, 'rb') as f:
        #     ct = joblib.load(file2)


        # Encoder les variables catégorielles
        encoder = OneHotEncoder()
        categorical_columns = ['Manufacturer', 'Category', 'Gear box type', 'Fuel type','Drive wheels','Model']
        encoded_test_data = ct.transform(df[categorical_columns])
        encoded_test_df = pd.DataFrame(encoded_test_data.toarray(), columns=encoder.get_feature_names(categorical_columns))

        # Concaténer les données encodées avec les autres variables
        test_data_encoded = pd.concat([df.drop(categorical_columns, axis=1), encoded_test_df], axis=1)

        # Faire une prédiction sur les nouvelles données
        y_pred = model.predict(test_data_encoded)

        # Afficher les prédictions
        print(y_pred)
                # Retourner la réponse
        return Response({'predicted_value': y_pred}, status=status.HTTP_200_OK)
    