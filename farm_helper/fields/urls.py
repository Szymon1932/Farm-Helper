from django.urls import path
from .views import viewsFertilizer, viewsClassField
from django.conf.urls.static import static

urlpatterns = [
    path('', viewsFertilizer.index, name='index'),

    # fertilizers
    path('fertilizers/', viewsFertilizer.show_fertilizers, name='show-fertilizers'),
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
]
