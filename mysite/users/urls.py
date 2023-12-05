from users import views
from django.urls import path

app_name = 'users'
urlpatterns = [
    
    # orders
    path('orders/<int:id>/<int:pdcd>/<str:user>/', views.Orders, name='orders'),

    # updating customer orders
    path('upd_orders/<int:id>/<int:upd_order_id>/', views.update_orders, name='upd_orders'),

    # customer rating-feedback view
    path('crf/<int:it_id>/<int:pc>/', views.CusRatFeed, name='CusRatFeed'),

    # updating customer ratings and feedbacks
    path('crf_upd/<int:details_id>/<int:crf_id>/', views.update_crf, name='upd_crf'),

    # deleting customer ratings and feedbacks
    path('del_crf/<int:details_id>/<int:crf_id>/', views.delete_crf, name='del_crf'),

    # paypal checkout button
    path('buy/<int:amt>/<int:qnt>/', views.Payment, name='buy'),

    # paypal on approve
    path('oa/', views.OnApprove, name='oa'),

    # paypal payment success
    path('ps/', views.PaymentSuccess, name='ps'),
]
