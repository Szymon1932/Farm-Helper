from django.shortcuts import render, redirect
from ..models import *
from ..forms import *
from django.contrib import messages

def show_fertilization_plans(request):
    fertilization_plans = FertilizationPlan.objects.all()
    return render(request, 'fields/show/fertilizationPlan.html', {'fertilization_plans': fertilization_plans})


def index(request):
    return render(request, 'fields/index.html')


def add_fertilization_plan(request):
    add_fertilization_plan = CreateFertilizationPlan()
    if request.method == 'POST':
        add_fertilization_plan = CreateFertilizationPlan(
            request.POST, request.FILES)
        if add_fertilization_plan.is_valid():
            if(add_fertilization_plan.cleaned_data['fertilizer_mass']>0):
                fertilization_plan = FertilizationPlan.objects.create(
                    predicted_crop=add_fertilization_plan.cleaned_data['predicted_crop'],
                    fertilizer=add_fertilization_plan.cleaned_data['fertilizer'],
                    fertilizer_mass=add_fertilization_plan.cleaned_data['fertilizer_mass'],
                    )
                fertilization_plan.save()
                return redirect('show-fertilization_plans')
            else:
                messages.success(request, ("Błąd podczas wprowadzania danych"))
                return redirect('show-fertilization_plans')
        else:
            messages.success(request, ("Błąd podczas wprowadzania danych"))
            return redirect('show-fertilization_plans')
    else:
        return render(request, 'fields/add/addFertilizationPlan.html', {'upload_form': add_fertilization_plan})


def update_fertilization_plan(request, fertilization_plan_id):
    fertilization_plan_id = int(fertilization_plan_id)
    try:
        fertilization_plan_obj = FertilizationPlan.objects.get(
            id=fertilization_plan_id)
    except FertilizationPlan.DoesNotExist:
        return redirect('show-fertilization_plans')
    fertilization_plan_form = CreateFertilizationPlan(
        request.POST or None, instance=fertilization_plan_obj)
    if fertilization_plan_form.is_valid():
        if(fertilization_plan_form.cleaned_data['fertilizer_mass']>0):
            fertilization_plan_form.save()
            return redirect('show-fertilization_plans')
        else:
            messages.success(request, ("Błąd podczas wprowadzania danych"))
            return redirect('show-fertilization_plans')
    return render(request, 'fields/add/addFertilizationPlan.html', {'upload_form': fertilization_plan_form})


def delete_fertilization_plan(request, fertilization_plan_id):
    fertilization_plan_id = int(fertilization_plan_id)
    try:
        fertilization_plan_obj = FertilizationPlan.objects.get(
            id=fertilization_plan_id)
    except FertilizationPlan.DoesNotExist:
        return redirect('show-fertilization_plans')
    fertilization_plan_obj.delete()
    return redirect('show-fertilization_plans')
