from datetime import datetime, timedelta
from django.shortcuts import  redirect
from ..models import Plant, PlantPrice
from django.db import transaction
from scipy import stats
import calendar
import numpy as np
from .getElements import *



def model(x,y, x_max):
    X=np.asarray(x, dtype=float)
    Y=np.asarray(y, dtype=float)
    slope, intercept, r, p, std_err = stats.linregress(X, Y)
    y_max = slope * x_max + intercept 
    print(r)
    return y_max



def predict_price(request):
    dates=[]
    dates_timestamp=[]
    X = []
    Y = []
    obj=[]

    PlantPrice.objects.filter(is_predicted=1).delete()

    all_plants=get_all_plant_names()
    for i in all_plants:
        for p in get_all_previous_prices():
            if str(p.plant).lower() == str(i).lower() :
                timestamp = int(calendar.timegm(p.date.timetuple()))
                dates.append(datetime.utcfromtimestamp(timestamp))
                dates_timestamp.append(timestamp)
                Y.append(p.price)
        dates.sort()
        dates_timestamp.sort()
        date_to_predict=max(dates) +timedelta(days=90)
        
        date_to_predict_timestamp=int(calendar.timegm(date_to_predict.timetuple()))
        X=dates_timestamp

        future_price = model(X,Y,date_to_predict_timestamp)

        obj.append(PlantPrice(
            plant=Plant.objects.get(plant_name=i.capitalize()),
            date=date_to_predict,
            price=future_price,
            is_predicted=1))

    with transaction.atomic():
        PlantPrice.objects.bulk_create(obj)

    return redirect('show-plant_prices')
