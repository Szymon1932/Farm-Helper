from datetime import datetime
import requests
from django.shortcuts import render, redirect
from ..models import Plant, PlantPrice


def get_price_from_source():
    r = requests.get(
        'https://www.farmer.pl/wykres/dane/zbozawykres/1/zbozawykres')
    data = r.json()
    xAxis = data['xAxis']
    el = xAxis['categories']
    dates = []
    names = []
    val_temp = []
    for i in el:
        dates.append(str(datetime.fromtimestamp(
            int(i/1000)).strftime('%Y-%m-%d')))
    values = {}
    for i, element in enumerate(data['series']):
        names.append(element['name'])
        for j, val in enumerate(element['data']):
            val_temp.append((dates[j], val))
        values.update({names[i]: val_temp})
    return values


def format_prices_to_database():
    values = get_price_from_source()
    keys = values.keys()
    output = []

    for keys in keys:
        for k, v in values.items():
            if k == keys:
                for v1, v2 in v:
                    if v2 != None:
                        # ('Rzepak', '2021-12-22 00:00:00', 3258.89)
                        output.append((k, v1, v2))

    return output  # zwraca list of tuples: (Roslina, data, cena, )


def get_plant_id(plant_name):
    # pass
    try:
        plant = Plant.objects.get(plant_name=plant_name)
        return plant.id
    except plant.DoesNotExist:
        pass


def auto_add_prices(request):

    # class PlantPrice(models.Model):
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    # date = models.DateField()
    # plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    # is_predicted = models.BooleanField()

    # class Meta:
    #     db_table = 'PlantPrice'
    output = format_prices_to_database()
    for (name, date, price) in (output):
        #plant_id = get_plant_id(name)
        add_plant_price = PlantPrice(
            plant=Plant.objects.get(plant_name=name),
            date=date,
            price=price,
            is_predicted=0)
        add_plant_price.save()
    redirect('show-plant_prices')
