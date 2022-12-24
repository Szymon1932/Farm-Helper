from django.shortcuts import render, redirect
from ..models import *
from ..forms import *
from django.http import HttpResponse
from django.contrib import messages

def show_predicted_crops(request):
    predicted_crops = PredictedCrop.objects.all()
    return render(request, 'fields/show/predictedCrop.html', {'predicted_crops': predicted_crops})


def index(request):
    return render(request, 'fields/index.html')


def add_predicted_crop(request):
    add_predicted_crop = CreatePredictedCrop()
    if request.method == 'POST':
        add_predicted_crop = CreatePredictedCrop(request.POST, request.FILES)
        if add_predicted_crop.is_valid():
            if(add_predicted_crop.cleaned_data['crop_mass']>0):
                predicted_crop = PredictedCrop.objects.create(
                    predicted_crop_name=add_predicted_crop.cleaned_data['predicted_crop_name'],
                    plant=add_predicted_crop.cleaned_data['plant'],
                    crop_mass=add_predicted_crop.cleaned_data['crop_mass'],
                    class_field=add_predicted_crop.cleaned_data['class_field'],
                    )
                predicted_crop.save()
                return redirect('show-predicted_crops')
            else:
                messages.success(request, ("Błąd podczas wprowadzania danych"))
                return redirect('show-predicted_crops')
        else:
            return HttpResponse("""Błędne dane. <a href = "{{ url : 'show-predicted_crops'}}">Odśwież</a>""")
    else:
        return render(request, 'fields/add/addPredictedCrop.html', {'upload_form': add_predicted_crop})


def update_predicted_crop(request, predicted_crop_id):
    predicted_crop_id = int(predicted_crop_id)
    try:
        predicted_crop_obj = PredictedCrop.objects.get(id=predicted_crop_id)
    except PredictedCrop.DoesNotExist:
        return redirect('show-predicted_crops')
    predicted_crop_form = CreatePredictedCrop(
        request.POST or None, instance=predicted_crop_obj)
    if predicted_crop_form.is_valid():
        if(predicted_crop_form.cleaned_data['crop_mass']>0):
            predicted_crop_form.save()
            return redirect('show-predicted_crops')
        else:
            messages.success(request, ("Błąd podczas wprowadzania danych"))
            return redirect('show-predicted_crops')
    else:
        return render(request, 'fields/add/addPredictedCrop.html', {'upload_form': predicted_crop_form})


def delete_predicted_crop(request, predicted_crop_id):
    predicted_crop_id = int(predicted_crop_id)
    try:
        predicted_crop_obj = PredictedCrop.objects.get(id=predicted_crop_id)
    except PredictedCrop.DoesNotExist:
        return redirect('show-predicted_crops')
    predicted_crop_obj.delete()
    return redirect('show-predicted_crops')
