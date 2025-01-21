from django.urls import path
from . import views 

urlpatterns = [
    path('', views.item_list, name="item_list"),
    path('create/', views.item_create, name='item_create')
]
