from django.urls import path,include
from .views import *

app_name = 'checkout'


urlpatterns = [
    path('checkout',  CheckoutView.as_view(), name='checkout'),
    

]