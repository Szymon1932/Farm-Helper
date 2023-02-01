import random
from django.shortcuts import redirect
from ..models import Plant
from django.db import transaction


def add_plant_auto(request):
    Plant.objects.all().delete()
    names = ['Pszenica konsumpcyjna', 'Kukurydza mokra', 'Kukurydza sucha', 'Żyto konsumpcyjne', 'Pszenżyto',
             'Jęczmień paszowy', 'Rzepak', 'Żyto paszowe', 'Owies', 'Jęczmień konsumpcyjny', 'Pszenica paszowa']
    
    obj=[]
    for name in names:
        try:
            obj.append(Plant(
                plant_name=name,
                seed_price=random.randrange(500,800)))
        except:
            pass

    with transaction.atomic():
        Plant.objects.bulk_create(obj)
    return redirect('show-plants') 
