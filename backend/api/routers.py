from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'manufacturer', ManufacturerViewSet, basename='manufacturer')


router.register(r'model/<str:manufacturer_libele>', ModelViewSet, basename='model')


router.register(r'category', CategoryViewSet, basename='category')


router.register(r'cylinders', CylindersViewSet, basename='cylinders')


router.register(r'fuels', FuelViewSet, basename='fuels')


router.register(r'drivewheels', DrivewheelsViewSet, basename='drivewheels')


router.register(r'gearbox', GearboxViewSet, basename='gearbox')


router.register(r'door', DoorViewSet, basename='door')


urlpatterns = router.urls