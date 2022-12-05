from django.shortcuts import render, redirect
from .models import Fertilizer
from .forms import CreateFertilizer
from django.http import HttpResponse


def index(request):
    fertilizers = Fertilizer.objects.all()
    return render(request, 'fields/fertilizer.html', {'fertilizers': fertilizers})


def add_fertilizer(request):
    add_fertilizer = CreateFertilizer()
    if request.method == 'POST':
        add_fertilizer = CreateFertilizer(request.POST, request.FILES)
        if add_fertilizer.is_valid():
            add_fertilizer.save()
            return redirect('index')
        else:
            return HttpResponse("""Błędne dane. <a href = "{{ url : 'index'}}">Odśwież</a>""")
    else:
        return render(request, 'fields/addFertilizer.html', {'add_fertilizer': add_fertilizer})


def update_fertilizer(request, fertilizer_id):
    fertilizer_id = int(fertilizer_id)
    try:
        fertilizer_obj = Fertilizer.objects.get(id=fertilizer_id)
    except Fertilizer.DoesNotExist:
        return redirect('index')
    fertilizer_form = CreateFertilizer(
        request.POST or None, instance=fertilizer_obj)
    if fertilizer_form.is_valid():
        fertilizer_form.save()
        return redirect('index')
    return render(request, 'fields/addFertilizer.html', {'upload_form': fertilizer_form})


def delete_fertilizer(request, fertilizer_id):
    fertilizer_id = int(fertilizer_id)
    try:
        fertilizer_get = Fertilizer.objects.get(id=fertilizer_id)
    except Fertilizer.DoesNotExist:
        return redirect('index')
    fertilizer_get.delete()
    return redirect('index')
