from datetime import datetime, timedelta
import requests
from django.shortcuts import render, redirect
from ..models import Plant, PlantPrice
from django.db import transaction
from scipy import stats
import calendar
import numpy as np

plant_prices_obj = PlantPrice.objects.all()


def retrieve_plant_names(): #getting all plant names
    plant_name = []
    for p in plant_prices_obj:
        plant_name.append(p.plant)
    return set(plant_name)


def model(x,y, x_max):
    X=np.asarray(x, dtype=float)
    Y=np.asarray(y, dtype=float)
    slope, intercept, r, p, std_err = stats.linregress(X, Y)
    y_max = slope * x_max + intercept #predicted price
    print(r)
    return y_max



def predict_price(request):
    dates=[]
    dates_timestamp=[]
    X = []
    Y = []
    obj=[]
    #PlantPrice.filter(is_predicted=1).delete() #delete predictions
    # mamy wszystkie ceny
    # teraz musimy DLA KAZDEGO PLANTA przewidzieć cenę bazującą na cenach poprzednich
    # zebrac wszystkie ceny w listę (key rośliny, cena)
    

    #zmienić X na datę cyfrową (predykcja będzie jednolita)
    all_plants=retrieve_plant_names()
    for i in all_plants:
        for p in plant_prices_obj:
            if p.plant == i and p.is_predicted==0:
                timestamp = int(calendar.timegm(p.date.timetuple()))
                dates.append(datetime.utcfromtimestamp(timestamp)) #good
                dates_timestamp.append(timestamp)
                Y.append(p.price)
        #get max date
        dates.sort()
        dates_timestamp.sort()
        #X=range(0,max_date_index)
        date_to_predict=max(dates) +timedelta(days=180)
        #conv date to timestamp
        date_to_predict_timestamp=int(calendar.timegm(date_to_predict.timetuple()))
        X=dates_timestamp
        #machine learinig predict price
        future_price = model(X,Y,date_to_predict_timestamp)
        print((i,datetime.utcfromtimestamp(date_to_predict_timestamp),future_price))
    #     obj.append(PlantPrice(
    #         plant=Plant.objects.get(plant_name=i),
    #         date=date_to_predict,
    #         price=future_price,
    #         is_predicted=1))
    
    # with transaction.atomic():
    #     PlantPrice.objects.bulk_create(obj)
    return redirect('show-plant_prices')
