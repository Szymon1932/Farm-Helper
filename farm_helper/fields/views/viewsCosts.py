# Koszty = Cena nawozu (per tona) * ilosc nawozu(tona) + Cena rośliny (per tona) * ilosc rośliny(tona)
# pobrać cenę nawozu i ilość nawozu
from django.shortcuts import render, redirect
from ..models import FertilizationPlan, Fertilizer, Plant, PredictedCrop
from django.http import HttpResponse


def home(request):
    #all_fertilizers = Fertilizer.objects.all
    all_predicted_crops = []
    all_predicted_crops = PredictedCrop.objects.all()  # retrieving all predicted crops
    prediction_and_cost = []  # list of tuples (pred_crop, value)
    for predicted_crop in all_predicted_crops:  # counting fertilization cost of prediction
        cost_fert = cost_of_fertilization(predicted_crop.id)
        cost_seed = cost_of_seed(predicted_crop.plant)
        cost_sum = cost_fert + cost_seed
        prediction_and_cost.append(
            (predicted_crop, cost_fert, cost_seed, cost_sum))
    print(prediction_and_cost)
    return render(request, 'fields/show/viewsCosts.html', {'all_prediction_and_cost': prediction_and_cost})

# show


def cost_of_fertilization(pred_crop_id):
    all_fert_plans = FertilizationPlan.objects.filter(
        predicted_crop_id=pred_crop_id)  # id of fertilization plans
    # fert plans contains fertilizer and fert mass
    # access to fertilizer by its id
    cost = 0
    # getting cost of all fertilizers (by crop_id)
    for f in all_fert_plans:
        cost += get_fertilizer_price(f.fertilizer_id) * f.fertilizer_mass
    return cost


def cost_of_seed(plant_n):
    cost = 0
    # getting cost of seed (by crop_id)
    try:
        plant = Plant.objects.get(plant_name=plant_n)
        plant_price = plant.seed_price
        return plant_price
    except Plant.DoesNotExist:
        pass


def get_fertilizer_price(fertilizer_id):  # getting fertilizers
    try:
        fertilizer = Fertilizer.objects.get(id=fertilizer_id)
        fert_price = fertilizer.price
        return fert_price
    except Fertilizer.DoesNotExist:
        pass

# todo
# zebrac tablice nawozy korespondujące do crop id = 1
