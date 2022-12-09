# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class User(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)

    class Meta:
        db_table = 'User'


class ClassField(models.Model):
    class_name = models.CharField(max_length=10)

    class Meta:
        db_table = 'ClassField'

    def __str__(self):
        return self.class_name


class Plant(models.Model):
    plant_name = models.CharField(max_length=50)
    seed_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'Plant'

    def __str__(self):
        return self.plant_name


class Fertilizer(models.Model):
    fertilizer_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'Fertilizer'

    def __str__(self):
        return self.fertilizer_name


class PlantPrice(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    is_predicted = models.BooleanField()

    class Meta:
        db_table = 'PlantPrice'


class PredictedCrop(models.Model):
    #name = models.CharField(max_length=50)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    crop_mass = models.DecimalField(max_digits=10, decimal_places=2)
    # Field renamed because it was a Python reserved word.
    class_field = models.ForeignKey(
        ClassField, on_delete=models.CASCADE, db_column='class_id')

    class Meta:
        db_table = 'PredictedCrop'


class FertilizationPlan(models.Model):
    #name = models.CharField(max_length=50)
    predicted_crop = models.ForeignKey(
        'PredictedCrop', on_delete=models.CASCADE)
    fertilizer = models.ForeignKey('Fertilizer', on_delete=models.CASCADE)
    fertilizer_mass = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'FertilizationPlan'


class Field(models.Model):
    #name = models.CharField(max_length=50)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    fertilization_plan = models.ForeignKey(
        FertilizationPlan, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Field'

# how to save this only for specific user
# users taken from program
