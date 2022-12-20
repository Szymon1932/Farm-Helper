from datetime import datetime
import requests
from django.shortcuts import render, redirect
from ..models import Plant, PlantPrice


def get_plant_price_id(plant_name):
    # pass
    try:
        plant = Plant.objects.get(plant_name=plant_name)
        return plant.id
    except plant.DoesNotExist:
        pass


def get_data():
    pass


def auto_predict_prices(request):
    x = []
    y = []
    plant_prices = []

    plant_prices_obj = PlantPrice.objects.all()
    # mamy wszystkie ceny
    # teraz musimy DLA KAZDEGO PLANTA przewidzieć cenę bazującą na cenach poprzednich
    # zebrac wszystkie ceny w listę (key rośliny, cena)
    for p in plant_prices_obj:
        plant_prices.append((str(p.plant), p.date.isoformat(), float(p.price)))
    print(plant_prices)
