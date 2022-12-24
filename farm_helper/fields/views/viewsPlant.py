from django.shortcuts import render, redirect
from ..models import Plant
from ..forms import CreatePlant
from django.http import HttpResponse
from django.contrib import messages

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
            if(add_plant.cleaned_data['seed_price']>0):
                plant = Plant.objects.create(
                plant_name=add_plant.cleaned_data['plant_name'],
                seed_price=add_plant.cleaned_data['seed_price']
                )
                plant.save()
                return redirect('show-plants')
            else:
                messages.success(request, ("Błąd podczas wprowadzania danych"))
                return redirect('show-plants')
        else:
            return redirect('show-plants')
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
        if(plant_form.cleaned_data['seed_price']>0):
            plant_form.save()
            return redirect('show-plants')
        else:
            messages.success(request, ("Błąd podczas wprowadzania danych"))
            return redirect('show-plants')
    else:
        return render(request, 'fields/add/addPlant.html', {'upload_form': plant_form})


def delete_plant(request, plant_id):
    plant_id = int(plant_id)
    try:
        plant_get = Plant.objects.get(id=plant_id)
    except Plant.DoesNotExist:
        return redirect('show-plants')
    plant_get.delete()
    return redirect('show-plants')
