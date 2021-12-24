from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

# Create your models here.


LABELS=(('new','new'),('sale','sale'),('hot','hot'),('','default'))
STOCK=(('in','In Stock'),('out of stock','Out Of Stock'))
STATUS=(('active','active'),('','Not active'))
class Category(models.Model):
    name=models.CharField(max_length=400) 
    slug=models.CharField(max_length=500,unique=True)
    description=models.TextField(blank=True)
    status=models.CharField(choices=STATUS,max_length=100,blank= True)
    rank = models.IntegerField(default = 1)
    
    def __str__(self):
	    return self.name


class Brand(models.Model):
	name = models.CharField(max_length=200)
	image=models.ImageField(upload_to='media',null=True)
	slug=models.CharField(max_length=500,unique=True)
	url = models.URLField(blank = True)
	def __str__ (self):
		return self.name
   

    	

class Slider(models.Model):
	title=models.CharField(max_length=400)
	subtitle= models.CharField(max_length= 300, default=1)
	image=models.ImageField(upload_to='media')
	status=models.CharField(choices=STATUS,max_length=100,blank= True)
	url=models.URLField(blank=True)
	rank=models.IntegerField(default=1)
	def __str__(self):
		return self.title
	

class Ad(models.Model):
	title = models.CharField(max_length = 500)
	image = models.ImageField(upload_to = 'media')
	url = models.URLField(blank = True)
	rank = models.IntegerField(default = 1,)
	def __str__(self):
		return self.title

class Item(models.Model):
	name = models.TextField()
	slug = models.CharField(max_length = 500, unique = True)
	description = models.TextField(blank = True)
	category = models.ForeignKey(Category,on_delete=models.CASCADE, default = 1)
	#subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, default = 1)
	rank = models.IntegerField(default = 1)
	price = models.IntegerField()
	discounted_price = models.IntegerField(default = 0)
	image = models.ImageField(upload_to = 'media',null = True)
	labels = models.CharField(choices = LABELS,max_length = 100,blank = True)
	status = models.CharField(choices = STATUS,max_length = 100,blank = True)
	stock = models.CharField(choices = STOCK,max_length = 100,blank = True)

	def __str__(self):
		return self.name

	def get_item_url(self):
		return reverse('home:detail',kwargs={'slug':self.slug})

	def get_cart_url(self):
		return reverse('cart:add-to-cart',kwargs={'slug':self.slug})    


class Contact(models.Model):
	name = models.CharField(max_length=300)
	email = models.CharField(max_length=500)
	subject = models.TextField()
	message = models.TextField()
	address = models.TextField(default=0)
	phone = models.IntegerField(default=0)
	def __str__ (self):
		return self.name




  


    
    