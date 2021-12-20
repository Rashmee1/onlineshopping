from django.urls import path,include
from .views import *

app_name = 'home'


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('detail/<slug>', ItemDetailView.as_view(), name='detail'),
    path('contact/', contact, name='contact'),
    path('shop/', shop, name='shop'),
    path('signup/', signup, name='signup'),
    path('single/', single, name='single'),
   

    
    

  
   
    
    
] 