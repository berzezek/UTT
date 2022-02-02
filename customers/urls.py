from django.urls import path
from .views import (
    customer_update,
    index, 
    customers, 
    old_customers,
    customer_add, 
    customer_detail,
    payments, 
    couchs, 
    couch_detail, 
    couch_add, 
    payment_add,
    )

urlpatterns = [
    path('', index, name='home'),
    path('customers/', customers, name='customers'),
    path('old_customers/', old_customers, name='old_customers'),
    path('customer_add/', customer_add, name='customer_add'),
    path('customer/<int:c_pk>/', customer_detail, name='customer_detail'),
    path('customer/<int:c_pk>/payments/', payments, name='payments'),
    path('customer/<int:c_pk>/payment_add/', payment_add, name='payment_add'),
    path('customer/<int:c_pk>/customer_update/', customer_update, name='customer_update'),
    path('couchs/', couchs, name='couchs'),
    path('couch/<int:couch_pk>/', couch_detail, name='couch_detail'),
    path('couch_add/', couch_add, name='couch_add'),
]