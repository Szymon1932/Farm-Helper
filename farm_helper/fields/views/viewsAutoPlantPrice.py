from datetime import datetime
import requests
from django.shortcuts import render, redirect
from ..models import Plant, PlantPrice
from django.db import transaction
from django.contrib import messages

def get_price_from_source():
    r = requests.get(
        'https://www.farmer.pl/wykres/dane/zbozawykres/101/zbozawykres')
    data = r.json()
    xAxis = data['xAxis']
    el = xAxis['categories']
    dates = []
    names = []
    val_temp = []
    for i in el:
        dates.append(str(datetime.fromtimestamp(
            int(i/1000)).strftime('%Y-%m-%d')))
    values = []
    for i, element in enumerate(data['series']):
        names.append(element['name'])
        for j, val in enumerate(element['data']):
            if val != None:
                val_temp.append((names[i], dates[j], val))
    return val_temp


def auto_add_prices(request):

    output = get_price_from_source()
    obj = []
    for (name, date, price) in (output):
        try:
            obj.append(PlantPrice(
                plant=Plant.objects.get(plant_name=name),
                date=date,
                price=price,
                is_predicted=0))
        except:
            messages.success(request, ("Błąd podczas wprowadzania danych"))
            return redirect('index')

    with transaction.atomic():
        PlantPrice.objects.bulk_create(obj)
    return redirect('show-plant_prices')