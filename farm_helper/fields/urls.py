from django.urls import path
from .views import viewsFertilizer
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
         viewsFertilizer.delete_fertilizer)

]
