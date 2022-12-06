from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),

    # fertilizers
    path('fertilizers/', views.show_fertilizers, name='show-fertilizers'),
    path('fertilizers/add_element/', views.add_fertilizer, name='add-fertilizer'),
    path('fertilizers/update/<int:fertilizer_id>', views.update_fertilizer),
    path('fertilizers/delete/<int:fertilizer_id>', views.delete_fertilizer)

]
