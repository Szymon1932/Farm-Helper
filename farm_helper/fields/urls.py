from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('add_element/', views.add_fertilizer, name='add-fertilizer'),
    path('update/<int:book_id>', views.update_fertilizer),
    path('delete/<int:book_id>', views.delete_fertilizer)
]