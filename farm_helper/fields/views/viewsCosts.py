# Koszty = Cena nawozu (per tona) * ilosc nawozu(tona) + Cena rośliny (per tona) * ilosc rośliny(tona)
# pobrać cenę nawozu i ilość nawozu
from django.shortcuts import render, redirect
from ..models import FertilizationPlan, Fertilizer, PredictedCrop
from django.http import HttpResponse


def home(request):
    #all_fertilizers = Fertilizer.objects.all
    all_predicted_crops = []
    all_predicted_crops.append(Fertilizer.objects.get(id=2))
    return render(request, 'fields/show/viewsCosts2.html', {'all_fertilizers': crop_fertilization_plans(5)})


def crop_fertilization_plans(pred_crop_id):
    all_fert_plans = FertilizationPlan.objects.filter(
        predicted_crop_id=pred_crop_id)  # id of fertilization plans
    # fert plans contains fertilizer and fert mass
    # access to fertilizer by its id
    cost = 0
    # getting cost of all fertilizers (by crop_id)
    for f in all_fert_plans:
        cost += get_fertilizer_price(f.fertilizer_id) * f.fertilizer_mass
    return cost


def get_fertilizer_price(fertilizer_id):  # getting fertilizers
    try:
        fertilizer = Fertilizer.objects.get(id=fertilizer_id)
        fert_price = fertilizer.price
        return fert_price
    except Fertilizer.DoesNotExist:
        pass

# todo
# zebrac tablice nawozy korespondujące do crop id = 1
