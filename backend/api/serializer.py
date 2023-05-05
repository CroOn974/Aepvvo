from rest_framework import serializers
from api.models import Category, Cylinders, Door, Drivewheels , Fuel, Gearbox, Manufacturer, Model 

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ['model_libele']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CylindersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cylinders
        fields = '__all__'

class FuelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuel
        fields = '__all__'

class DrivewheelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drivewheels
        fields = '__all__'


class GearboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gearbox
        fields = '__all__'


class DoorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Door
        fields = '__all__'

class PredictSerializer(serializers.ModelSerializer):
    manufacturer  = serializers.CharField()
    model  = serializers.CharField()
    year = serializers.IntegerField()
    category  = serializers.CharField()
    fuelType  = serializers.CharField()
    mileage = serializers.IntegerField()
    gearBoxList  = serializers.CharField()
    engine  = serializers.CharField()
    leather  = serializers.CharField()
    airbag  = serializers.CharField()
    levy  = serializers.CharField()
    cylinders  = serializers.CharField()

    class Meta:
        fields = ['manufacturer','model','year','category','fuelType','mileage','gearBoxList','engine','leather','airbag','levy','cylinders']
