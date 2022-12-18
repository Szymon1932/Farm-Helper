import requests
from datetime import datetime
from django.shortcuts import render, redirect
from ..models import PlantPrice, Plant
from ..forms import CreatePlantPrice
from django.http import HttpResponse


def show_plant_prices(request):
    plant_prices = PlantPrice.objects.all()
    return render(request, 'fields/show/plantPrice.html', {'plant_prices': plant_prices})


def index(request):
    return render(request, 'fields/index.html')


def add_plant_price(request):
    add_plant_price = CreatePlantPrice()
    if request.method == 'POST':
        add_plant_price = CreatePlantPrice(request.POST, request.FILES)
        if add_plant_price.is_valid():
            add_plant_price.save()
            return redirect('show-plant_prices')  # name in urls
        else:
            return HttpResponse("""Błędne dane. <a href = "{{ url : 'show-plant_prices'}}">Odśwież</a>""")
    else:
        return render(request, 'fields/add/addPlantPrice.html', {'upload_form': add_plant_price})


def update_plant_price(request, plant_price_id):
    plant_price_id = int(plant_price_id)
    try:
        plant_price_obj = PlantPrice.objects.get(id=plant_price_id)
    except PlantPrice.DoesNotExist:
        return redirect('show-plant_prices')
    plant_price_form = CreatePlantPrice(
        request.POST or None, instance=plant_price_obj)
    if plant_price_form.is_valid():
        plant_price_form.save()
        return redirect('show-plant_prices')
    return render(request, 'fields/add/addPlantPrice.html', {'upload_form': plant_price_form})


def delete_plant_price(request, plant_price_id):
    plant_price_id = int(plant_price_id)
    try:
        plant_price_get = PlantPrice.objects.get(id=plant_price_id)
    except PlantPrice.DoesNotExist:
        return redirect('show-plant_prices')
    plant_price_get.delete()
    return redirect('show-plant_prices')


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
        dates.append(str(datetime.fromtimestamp(int(i/1000))))
    values = {}
    for i, element in enumerate(data['series']):
        names.append(element['name'])
        for j, val in enumerate(element['data']):
            val_temp.append((dates[j], val))
        values.update({names[i]: val_temp})
    return values


def format_prices_to_database(values):
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


def auto_add_prices(output):
    add_plant_price = CreatePlantPrice()
    for (name, date, price) in (output):
        pass  # to implementation
