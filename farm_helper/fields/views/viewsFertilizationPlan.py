from django.shortcuts import render, redirect
from ..models import *
from ..forms import *
from django.http import HttpResponse


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
            add_fertilization_plan.save()
            return redirect('show-fertilization_plans')  # name in urls
        else:
            return HttpResponse("""Błędne dane. <a href = "{{ url : 'show-fertilization_plans'}}">Odśwież</a>""")
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
        fertilization_plan_form.save()
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
