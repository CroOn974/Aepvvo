# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Car(models.Model):
    car_id = models.IntegerField(primary_key=True)
    car_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    car_levy = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    car_year = models.DateField(blank=True, null=True)
    car_leather = models.BooleanField(blank=True, null=True)
    car_engine_volume = models.CharField(max_length=50, blank=True, null=True)
    car_mileage = models.IntegerField()
    car_airbags = models.CharField(max_length=50, blank=True, null=True)
    car_turbo = models.BooleanField(blank=True, null=True)
    cylenders_number = models.ForeignKey('Cylinders', models.DO_NOTHING, db_column='cylenders_number')
    door_number = models.ForeignKey('Door', models.DO_NOTHING, db_column='door_number')
    drivewheels_type = models.ForeignKey('Drivewheels', models.DO_NOTHING, db_column='drivewheels_type')
    gearbox_type = models.ForeignKey('Gearbox', models.DO_NOTHING, db_column='gearbox_type')
    model_libele = models.ForeignKey('Model', models.DO_NOTHING, db_column='model_libele')
    fuel_type = models.ForeignKey('Fuel', models.DO_NOTHING, db_column='fuel_type')
    category_libele = models.ForeignKey('Category', models.DO_NOTHING, db_column='category_libele')

    class Meta:
        managed = False
        db_table = 'car'


class Category(models.Model):
    category_libele = models.CharField(primary_key=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'category'


class Cylinders(models.Model):
    cylenders_number = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'cylinders'


class Door(models.Model):
    door_number = models.CharField(primary_key=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'door'


class Drivewheels(models.Model):
    drivewheels_type = models.CharField(primary_key=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'drivewheels'


class Fuel(models.Model):
    fuel_type = models.CharField(primary_key=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'fuel'


class Gearbox(models.Model):
    gearbox_type = models.CharField(primary_key=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'gearbox'


class Manufacturer(models.Model):
    manufacturer_libele = models.CharField(primary_key=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'manufacturer'


class Model(models.Model):
    model_libele = models.CharField(primary_key=True, max_length=50)
    manufacturer_libele = models.ForeignKey(Manufacturer, models.DO_NOTHING, db_column='manufacturer_libele')

    class Meta:
        managed = False
        db_table = 'model'
