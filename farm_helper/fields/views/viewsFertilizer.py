from django.shortcuts import render, redirect
from ..models import Fertilizer
from ..forms import CreateFertilizer
from django.http import HttpResponse
from django.contrib import messages

def show_fertilizers(request):
    fertilizers = Fertilizer.objects.all()
    return render(request, 'fields/show/fertilizer.html', {'fertilizers': fertilizers})


def index(request):
    return render(request, 'fields/index.html')


def add_fertilizer(request):
    add_fertilizer = CreateFertilizer()
    if request.method == 'POST':
        add_fertilizer = CreateFertilizer(request.POST, request.FILES)
        
        if add_fertilizer.is_valid():
            if(add_fertilizer.cleaned_data['price']>0):
                fertilizer = Fertilizer.objects.create(
                fertilizer_name=add_fertilizer.cleaned_data['fertilizer_name'],
                price=add_fertilizer.cleaned_data['price']
                )
                fertilizer.save()
                return redirect('show-fertilizers')
            else:
                messages.success(request, ("Błąd podczas wprowadzania danych"))
                return redirect('show-fertilizers')
        else:
            messages.success(request, ("Błąd podczas wprowadzania danych"))
            return redirect('show-fields')
    else:
        return render(request, 'fields/add/addFertilizer.html', {'upload_form': add_fertilizer})


def update_fertilizer(request, fertilizer_id):
    fertilizer_id = int(fertilizer_id)
    try:
        fertilizer_obj = Fertilizer.objects.get(id=fertilizer_id)
    except Fertilizer.DoesNotExist:
        return redirect('show-fertilizers')
    fertilizer_form = CreateFertilizer(
        request.POST or None, instance=fertilizer_obj)
    if fertilizer_form.is_valid():
        if(fertilizer_form.cleaned_data['price']>0):
            fertilizer_form.save()
            return redirect('show-fertilizers')
        else:
            messages.success(request, ("Błąd podczas wprowadzania danych"))
            return redirect('show-fertilizers')
    return render(request, 'fields/add/addFertilizer.html', {'upload_form': fertilizer_form})


def delete_fertilizer(request, fertilizer_id):
    fertilizer_id = int(fertilizer_id)
    try:
        fertilizer_get = Fertilizer.objects.get(id=fertilizer_id)
    except Fertilizer.DoesNotExist:
        return redirect('show-fertilizers')
    fertilizer_get.delete()
    return redirect('show-fertilizers')
