from django.urls import path,include
from .views import *

app_name = 'cart'


urlpatterns = [
    path('cart',  CartView.as_view(), name='cart'),
    

]