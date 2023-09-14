from django.urls import path, include
from food import views

app_name = 'food'

urlpatterns = [
    path('home/', views.index, name='index'),
    path('detail/<int:item_id>/', views.detail, name='detail'),
    path('add/', views.create_item, name='create_item'),
]
