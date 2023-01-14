# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

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
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    date = models.DateField()
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    is_predicted = models.BooleanField()

    class Meta:
        db_table = 'PlantPrice'

    def __str__(self):
        return str(self.price)


class PredictedCrop(models.Model):
    predicted_crop_name = models.CharField(max_length=50)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    crop_mass = models.DecimalField(max_digits=10, decimal_places=2)
    class_field = models.ForeignKey(
        ClassField, on_delete=models.CASCADE, db_column='class_id')

    class Meta:
        db_table = 'PredictedCrop'

    def __str__(self):
        return self.predicted_crop_name


class FertilizationPlan(models.Model):
    predicted_crop = models.ForeignKey(
        'PredictedCrop', on_delete=models.CASCADE)
    fertilizer = models.ForeignKey('Fertilizer', on_delete=models.CASCADE)
    fertilizer_mass = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'FertilizationPlan'
    
    def __str__(self):
        return str(self.fertilizer_mass)

class Field(models.Model):
    field_name = models.CharField(max_length=50)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class_field = models.ForeignKey(
        ClassField, on_delete=models.CASCADE, db_column='class_id')

    class Meta:
        db_table = 'Field'
    def __str__(self):
        return self.field_name
