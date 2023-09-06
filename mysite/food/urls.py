from django.urls import path, include
from food import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('detail/<int:item_id>/', views.detail, name='detail'),
]
