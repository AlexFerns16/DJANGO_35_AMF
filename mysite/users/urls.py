from users import views
from django.urls import path

app_name = 'users'
urlpatterns = [
    
    # orders
    path('orders/<int:id>/<int:pdcd>/<str:user>/', views.Orders, name='orders'),
]
