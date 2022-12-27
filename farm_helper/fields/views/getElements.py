from ..models import ClassField, Fertilizer, Plant, PlantPrice
def get_all_plant_prices():
    plant_prices_obj = PlantPrice.objects.all()
    return plant_prices_obj

def get_all_plant_names():
    plant_names=[]
    for p in Plant.objects.all():
        plant_names.append(p.plant_name.lower())
    return set(plant_names) 

def get_all_fertilizer_names():
    fertilizer_names=[]
    for p in Fertilizer.objects.all():
        fertilizer_names.append(p.fertilizer_name.lower())
    return set(fertilizer_names) 
    
def cost_of_seed(plant_n):
    cost = 0
    try:
        plant = Plant.objects.get(plant_name=plant_n)
        plant_price = plant.seed_price
        return plant_price
    except Plant.DoesNotExist:
        pass


def get_fertilizer_price(fertilizer_id):
    try:
        fertilizer = Fertilizer.objects.get(id=fertilizer_id)
        fert_price = fertilizer.price
        return fert_price
    except Fertilizer.DoesNotExist:
        pass


def get_all_classes():
    classes=[]
    for p in ClassField.objects.all():
        classes.append(p.class_name)
    return set(classes)

def get_all_prices():
    plant_prices_obj = PlantPrice.objects.filter(is_predicted=1)
    return plant_prices_obj

def get_all_plants():
    plant_obj = Plant.objects.all()
    return plant_obj

def get_plant_id(plant_n):
    try:
        plant = Plant.objects.get(plant_name=plant_n)
        plant_id = plant.id
        return plant_id
    except Plant.DoesNotExist:
        pass


def get_plant_price(plant_n, predicted):
    try:
        id=get_plant_id(plant_n)
        obj = PlantPrice.objects.get(plant=int(id), is_predicted=predicted)
        obj_income = obj.price
        return obj_income
    except PlantPrice.DoesNotExist:
        pass

def get_fertilizer_price(fertilizer_id): 
    try:
        fertilizer = Fertilizer.objects.get(id=fertilizer_id)
        fert_price = fertilizer.price
        return fert_price
    except Fertilizer.DoesNotExist:
        pass
