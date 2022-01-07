from django.db import models

# Create your models here.
from django.db import models
from home.models import Item
from django.conf  import settings 
from django.urls  import reverse
from cart.models import Cart
from django.shortcuts import reverse
from django.db import models
from home.models import Item





# Create your models here.
class Checkoutform(models.Model):
	ordered_By = models.CharField(max_length=200)
	country = models.TextField()
	address = models.TextField(default =0)
	emailaddress = models.EmailField()
	phone = models.IntegerField(default=0)
	cart = models.ForeignKey(Cart, on_delete= models.CASCADE,default=0)
	items = models.ForeignKey(Item,on_delete = models.CASCADE,default=0) 
	
	
	def __str__ (self):
		return self.cart.user.username
		
class Totalcart(models.Model):
	cart = models.ForeignKey(Cart, on_delete= models.CASCADE,default=0)
	total = models.IntegerField(default=0)
	

	def __str__ (self):
		return self.cart.user.username	
	
        		
        	





   

