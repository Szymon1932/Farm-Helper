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
