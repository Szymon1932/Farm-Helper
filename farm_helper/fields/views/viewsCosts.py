from django.shortcuts import render
from ..models import FertilizationPlan, Plant, PredictedCrop
from .getElements import *


def home(request):
    all_predicted_crops = []
    all_predicted_crops = PredictedCrop.objects.all()  
    prediction_and_cost = []  
    for predicted_crop in all_predicted_crops:  
        cost_fert = cost_of_fertilization(predicted_crop.id)
        cost_seed = cost_of_seed(predicted_crop.plant)
        cost_sum = cost_fert + cost_seed
        prediction_and_cost.append(
            (predicted_crop, cost_fert, cost_seed, cost_sum))
    print(prediction_and_cost)
    return render(request, 'fields/show/viewsCosts.html', {'all_prediction_and_cost': prediction_and_cost})


def cost_of_fertilization(pred_crop_id):
    all_fert_plans = FertilizationPlan.objects.filter(
        predicted_crop_id=pred_crop_id) 
    cost = 0

    for f in all_fert_plans:
        cost += get_fertilizer_price(f.fertilizer_id) * f.fertilizer_mass #from getElements
    return cost


def cost_of_seed(plant_n):
    cost = 0
    try:
        plant = Plant.objects.get(plant_name=plant_n)
        plant_price = plant.seed_price
        return plant_price
    except Plant.DoesNotExist:
        pass


