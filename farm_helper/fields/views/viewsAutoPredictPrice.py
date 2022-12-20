from datetime import datetime
import requests
from django.shortcuts import render, redirect
from ..models import Plant, PlantPrice


plant_prices_obj = PlantPrice.objects.all()


def retrieve_plant_names():
    plant_name = []
    for p in plant_prices_obj:
        plant_name.append(p.plant)
    return set(plant_name)


def predict_plant_price(plant, plant_prices_obj):
    # machine learning
    dates = []
    prices = []
    # pick max date + half year to predict
    for p in plant_prices_obj:
        pass
    for p in plant_prices_obj:
        if p.is_predicted == 0 and p.plant == plant:
            prices.append[p.price]


def get_data():
    pass


def auto_predict_prices(request, plant_prices_obj):
    x = []
    y = []
    plant_prices = []

    # mamy wszystkie ceny
    # teraz musimy DLA KAZDEGO PLANTA przewidzieć cenę bazującą na cenach poprzednich
    # zebrac wszystkie ceny w listę (key rośliny, cena)
    for p in plant_prices_obj:
        plant_prices.append((str(p.plant), p.date.isoformat(), float(p.price)))
    print(plant_prices)
