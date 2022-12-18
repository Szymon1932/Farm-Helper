from django.shortcuts import render, redirect
#from ..models import Plant
from ..forms import CreatePlant
#from django.http import HttpResponse


def add_plant_auto(request):
    add_plant = CreatePlant()
    names = ['Pszenica konsumpcyjna', 'Kukurydza mokra', 'Kukurydza sucha', 'Żyto konsumpcyjne', 'Pszenżyto',
             'Jęczmień paszowy', 'Rzepak', 'Żyto paszowe', 'Owies', 'Jęczmień konsumpcyjny', 'Pszenica paszowa']
    iterator = 0
    price = 100.0
    if request.method == 'POST':
        for n in names:
            add_plant = CreatePlant(request.POST)
            add_plant.plant_name = n
            iterator = iterator + 1
            price = price * iterator
            add_plant.seed_price = price
            if add_plant.is_valid():
                add_plant.save()
    return redirect('show-plants')  # name in urls
