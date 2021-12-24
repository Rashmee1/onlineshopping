from django.urls import path,include
from .views import *

app_name = 'home'


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', contact, name='contact'),
    path('detail/<slug>', ProductView.as_view(), name='detail'),
    
    path('shop/<slug>', ShopView.as_view(), name='shop'),
    path('signup/', signup, name='signup'),
    
   

    
    

  
   
    
    
] 