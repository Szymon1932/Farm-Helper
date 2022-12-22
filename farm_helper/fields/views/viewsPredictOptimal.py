from ..models import ClassField, PlantPrice
from .viewsCosts import *

#predicting costs

def home():
    #all_fertilizers = Fertilizer.objects.all
    all_predicted_crops = []
    all_predicted_crops = PredictedCrop.objects.all()  # retrieving all predicted crops
    prediction_and_cost = []  # list of tuples (pred_crop, value)
    for predicted_crop in all_predicted_crops:  # counting fertilization cost of prediction
        cost_fert = cost_of_fertilization(predicted_crop.id)
        cost_seed = cost_of_seed(predicted_crop.plant)
        plant = predicted_crop.plant
        class_field = predicted_crop.class_field
        cost_sum = cost_fert + cost_seed
        prediction_and_cost.append(
            (plant, class_field, cost_sum))
    return (prediction_and_cost) #cost_sum is good
    #return render(request, 'fields/show/viewsCosts.html', {'all_prediction_and_cost': prediction_and_cost})

#getting all classes
#ClassField
def get_all_classes():
    classes=[]
    for p in ClassField.objects.all():
        classes.append(p.class_name)
    return set(classes) #lista klas

def get_all_prices():
    plant_prices_obj = PlantPrice.objects.filter(is_predicted=1)
    return plant_prices_obj

def get_all_plants():
    plant_obj = Plant.objects.all()
    return plant_obj

def get_plant_id(plant_n):
    cost = 0
    # getting cost of seed (by crop_id)
    try:
        plant = Plant.objects.get(plant_name=plant_n)
        plant_id = plant.id
        print(plant_id)
        return plant_id
    except Plant.DoesNotExist:
        pass


def get_income(plant_n):
    try:
        id=get_plant_id(plant_n)
        obj = PlantPrice.objects.get(plant=int(id), is_predicted=1)
        obj_income = obj.price
        return obj_income
    except PlantPrice.DoesNotExist:
        pass

def get_fertilizer_price(fertilizer_id):  # getting fertilizers
    try:
        fertilizer = Fertilizer.objects.get(id=fertilizer_id)
        fert_price = fertilizer.price
        return fert_price
    except Fertilizer.DoesNotExist:
        pass

def calculate_profit(request):
    all_costs=home()
    all_predicted_crops = []
    all_predicted_crops = PredictedCrop.objects.all() 
    all_plants = get_all_plants()

    all_prices=get_all_prices() #get prices of a plant (by plant(id))
    all_classes=get_all_classes()
    
    output=[] # plant, class, income
    for c in all_classes:
        for pl in all_plants: 
            for pc in all_predicted_crops:
                for (plant,class_field, cost) in all_costs:
                    if c == str(pc.class_field):
                        #print(c,pc.class_field)
                        
                        if str(pl.plant_name) == str(pc.plant):
                            if str(plant)==str(pc.plant): 
                                
                                income = pc.crop_mass * get_income(pc.plant) #check specific price
                                profit = income - cost
                                output.append((class_field, income, cost, profit))
    print(output, '\n')
    return redirect('show-plant_prices')

