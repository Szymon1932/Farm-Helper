from django.shortcuts import render, redirect
from ..models import PlantPrice
from ..forms import CreatePlantPrice
from django.contrib import messages

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
            if(add_plant_price.cleaned_data['price']>0):
                plant_price = PlantPrice.objects.create(
                price=add_plant_price.cleaned_data['price'],
                date=add_plant_price.cleaned_data['date'],
                plant=add_plant_price.cleaned_data['plant'],
                is_predicted=0
                )
                plant_price.save()
                return redirect('show-plant_prices')  # name in urls
            else:
                messages.success(request, ("Błąd podczas wprowadzania danych"))
                return redirect('show-plant_prices')
        else:
            messages.success(request, ("Błąd podczas wprowadzania danych"))
            return redirect('show-plant_prices')
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
        if(plant_price_form.cleaned_data['price']>0):
            plant_price_form.save()
            return redirect('show-plant_prices')
        else:
            messages.success(request, ("Błąd podczas wprowadzania danych"))
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
