from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

manufacturer = DefaultRouter()
manufacturer.register(r'manufacturer/', ManufacturerViewSet, basename='manufacturer')

model = DefaultRouter()
model.register(r'model/<str:manufacturer_libele>/', ModelViewSet, basename='model')

category = DefaultRouter()
category.register(r'category/', CategoryViewSet, basename='category')

cylinders = DefaultRouter()
cylinders.register(r'cylinders/', CylindersViewSet, basename='cylinders')

fuels = DefaultRouter()
fuels.register(r'fuels/', FuelViewSet, basename='fuels')

drivewheels = DefaultRouter()
drivewheels.register(r'drivewheels/', Drivewheels, basename='drivewheels')

gearbox = DefaultRouter()
gearbox.register(r'gearbox/', GearboxViewSet, basename='gearbox')

door = DefaultRouter()
door.register(r'door/', DoorViewSet, basename='door')

urlpatterns = [
    path('', include(manufacturer.urls)),
    path('', include(model.urls)),
    path('', include(category.urls)),
    path('', include(cylinders.urls)),
    path('', include(gearbox.urls)),
    path('', include(door.urls)),

]
