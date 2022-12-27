from .viewsCosts import *
from .getElements import *

def home():
    all_predicted_crops = []
    all_predicted_crops = PredictedCrop.objects.all() 
    prediction_and_cost = []
    for predicted_crop in all_predicted_crops:  
        cost_fert = cost_of_fertilization(predicted_crop.id)
        cost_seed = cost_of_seed(predicted_crop.plant)
        plant = predicted_crop.plant
        class_field = predicted_crop.class_field
        cost_sum = cost_fert + cost_seed
        prediction_and_cost.append(
            (predicted_crop, plant, class_field, cost_sum))
    return (prediction_and_cost) 

def show_profits(output):
    all_classes=get_all_classes()

    vals = []
    for c in all_classes:
        for class_field, profit, plant, income, cost, predicted_crop in output:
            if str(class_field) == str(c): 
                vals.append((plant, class_field, float(profit), income, cost, predicted_crop.predicted_crop_name))
                break
    return vals

def process_profit():
    all_costs=home()
    all_predicted_crops = []
    all_predicted_crops = PredictedCrop.objects.all() 
    all_classes=get_all_classes()
    
    output=[] 
    for c in all_classes:
        for pc in all_predicted_crops:
            for (predicted_crop, plant,class_field, cost) in all_costs:
                if predicted_crop.id == pc.id:
                    if c == str(pc.class_field) and c == str(class_field) and str(plant)==str(pc.plant):
                        income = pc.crop_mass * get_plant_price(pc.plant, 1)
                        profit = income - cost
                        output.append((str(pc.class_field),float(profit), plant, float(income), float(cost), predicted_crop ))

    output.sort(reverse=1)
    print(output)
    return output



def calculate_profit(request):
    output=process_profit()
    return render(request, 'fields/show/calculations.html', {'output': output})
    
def optimal_class_profit(request):
    output=process_profit()
    output=show_profits(output)
    return render(request, 'fields/show/optimalClass.html', {'output': output})