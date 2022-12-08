from django.urls import path
from .views import viewsFertilizer, viewsClassField, viewsPlant, viewsPlantPrice, viewsPredictedCrop
from django.conf.urls.static import static

urlpatterns = [
    path('', viewsFertilizer.index, name='index'),

    # fertilizers
    path('fertilizers/', viewsFertilizer.show_fertilizers,
         name='show-fertilizers'),
    path('fertilizers/add_element/',
         viewsFertilizer.add_fertilizer, name='add-fertilizer'),
    path('fertilizers/update/<int:fertilizer_id>',
         viewsFertilizer.update_fertilizer),
    path('fertilizers/delete/<int:fertilizer_id>',
         viewsFertilizer.delete_fertilizer),

    # class_fields

    path('class_fields/', viewsClassField.show_class_fields,
         name='show-class_fields'),
    path('class_fields/add_element/',
         viewsClassField.add_class_field, name='add-class_field'),
    path('class_fields/update/<int:class_field_id>',
         viewsClassField.update_class_field),
    path('class_fields/delete/<int:class_field_id>',
         viewsClassField.delete_class_field),

    # plants

    path('plants/', viewsPlant.show_plants,
         name='show-plants'),
    path('plants/add_element/',
         viewsPlant.add_plant, name='add-plant'),
    path('plants/update/<int:plant_id>',
         viewsPlant.update_plant),
    path('plants/delete/<int:plant_id>',
         viewsPlant.delete_plant),


    # plant_prices

    path('plant_prices/', viewsPlantPrice.show_plant_prices,
         name='show-plant_prices'),
    path('plant_prices/add_element/',
         viewsPlantPrice.add_plant_price, name='add-plant_price'),
    path('plant_prices/update/<int:plant_price_id>',
         viewsPlantPrice.update_plant_price),
    path('plant_prices/delete/<int:plant_price_id>',
         viewsPlantPrice.delete_plant_price),

    # predictedCrops

    path('predicted_crops/', viewsPredictedCrop.show_predicted_crops,
         name='show-predicted_crops'),
    path('predicted_crops/add_element/',
         viewsPredictedCrop.add_predicted_crop, name='add-predicted_crop'),
    path('predicted_crops/update/<int:predicted_crop_id>',
         viewsPredictedCrop.update_predicted_crop),
    path('predicted_crops/delete/<int:predicted_crop_id>',
         viewsPredictedCrop.delete_predicted_crop),

]
