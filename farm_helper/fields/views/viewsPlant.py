from django.shortcuts import render, redirect
from ..models import Plant
from ..forms import CreatePlant
from django.http import HttpResponse


def show_plants(request):
    plants = Plant.objects.all()
    return render(request, 'fields/show/plant.html', {'plants': plants})


def index(request):
    return render(request, 'fields/index.html')


def add_plant(request):
    add_plant = CreatePlant()
    if request.method == 'POST':
        add_plant = CreatePlant(request.POST, request.FILES)
        if add_plant.is_valid():
            add_plant.save()
            return redirect('show-plants')  # name in urls
        else:
            return HttpResponse("""Błędne dane. <a href = "{{ url : 'show-plants'}}">Odśwież</a>""")
    else:
        return render(request, 'fields/add/addPlant.html', {'upload_form': add_plant})


def update_plant(request, plant_id):
    plant_id = int(plant_id)
    try:
        plant_obj = Plant.objects.get(id=plant_id)
    except Plant.DoesNotExist:
        return redirect('show-plants')
    plant_form = CreatePlant(
        request.POST or None, instance=plant_obj)
    if plant_form.is_valid():
        plant_form.save()
        return redirect('show-plants')
    return render(request, 'fields/add/addPlant.html', {'upload_form': plant_form})


def delete_plant(request, plant_id):
    plant_id = int(plant_id)
    try:
        plant_get = Plant.objects.get(id=plant_id)
    except Plant.DoesNotExist:
        return redirect('show-plants')
    plant_get.delete()
    return redirect('show-plants')


def add_names_to_database():
    add_plant = CreatePlant()
    names = ['Pszenica konsumpcyjna', 'Kukurydza mokra', 'Kukurydza sucha', 'Żyto konsumpcyjne', 'Pszenżyto',
             'Jęczmień paszowy', 'Rzepak', 'Żyto paszowe', 'Owies', 'Jęczmień konsumpcyjny', 'Pszenica paszowa']
    iterator = 0
    price = 100
    for n in names:
        add_plant.plant_name = n
        iterator = iterator + 1
        price = price * iterator
        add_plant.seed_price = price
        add_plant.save()
    return redirect('show-plants')  # name in urls
