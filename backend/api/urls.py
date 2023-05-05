from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import CategoryViewSet, CylindersViewSet, DoorViewSet, DrivewheelsViewSet, FuelViewSet, GearboxViewSet, ManufacturerViewSet, ModelViewSet, PredictViewSet

manufacturer = DefaultRouter()
manufacturer.register(r'manufacturer', ManufacturerViewSet, basename='manufacturer')

model = DefaultRouter()
model.register(r'', ModelViewSet, basename='model')

category = DefaultRouter()
category.register(r'category', CategoryViewSet, basename='category')

cylinders = DefaultRouter()
cylinders.register(r'cylinders', CylindersViewSet, basename='cylinders')

fuels = DefaultRouter()
fuels.register(r'fuels', FuelViewSet, basename='fuels')

drivewheels = DefaultRouter()
drivewheels.register(r'drivewheels', DrivewheelsViewSet, basename='drivewheels')

gearbox = DefaultRouter()
gearbox.register(r'gearbox', GearboxViewSet, basename='gearbox')

door = DefaultRouter()
door.register(r'door', DoorViewSet, basename='door')

predict = DefaultRouter()
predict.register(r'predict', PredictViewSet, basename='predict')

urlpatterns = [
    path('', include(manufacturer.urls)),
    path('model/<str:manufacturer_libele>', include(model.urls)),
    path('', include(category.urls)),
    path('', include(cylinders.urls)),
    path('', include(drivewheels.urls)),
    path('', include(fuels.urls)),
    path('', include(gearbox.urls)),
    path('', include(door.urls)),
    path('', include(predict.urls)),

]
