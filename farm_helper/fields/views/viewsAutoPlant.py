import random
from django.shortcuts import render, redirect
from ..models import Plant
from django.db import transaction
# from ..forms import CreatePlant
#from django.http import HttpResponse


def add_plant_auto(request):
    Plant.objects.all().delete()
    names = ['Pszenica konsumpcyjna', 'Kukurydza mokra', 'Kukurydza sucha', 'Żyto konsumpcyjne', 'Pszenżyto',
             'Jęczmień paszowy', 'Rzepak', 'Żyto paszowe', 'Owies', 'Jęczmień konsumpcyjny', 'Pszenica paszowa']
    
    obj=[]
    for name in names:
        try:
            obj.append(Plant(
                plant_name=name,
                seed_price=random.randrange(50,150)))
        except:
            pass

    with transaction.atomic():
        Plant.objects.bulk_create(obj)
    return redirect('show-plants')  # name in urls
