from django.shortcuts import render,redirect
from django.views.generic import View
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings


# Create your views here.
class BaseView(View):
	views = {}


class HomeView(BaseView):
    def get(self,request):
        
        self.views['items'] = Item.objects.all()
        self.views['ads'] = Ad.objects.all()
        self.views['sliders'] = Slider.objects.all()
        self.views['category'] = Category.objects.all()
        self.views['brands'] = Brand.objects.all()
        return render(request,'index.html',self.views)

class ContactInfoView(BaseView):
    def get(self,request,slug):
        self.views['contactinfos'] = ContactInfo.objects.all()
        return render(request,'contact.html',self.views)
        






class ProductView(BaseView):
	def get(self,request,slug):
		self.views['category'] = Category.objects.all()
		
		self.views['items'] = Item.objects.all()

		

		return render(request,'single-product.html',self.views)

class ShopView(BaseView):
    def get(self,request,slug):
        self.views['items'] = Item.objects.all()
        self.views['category'] = Category.objects.all()
        return render(request,'shop.html',self.views)

	   
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        data = {
                'name' : name,
                'email' : email,
                'subject' : subject,
                'message' : message,
        }
        message = '''''
        New message: {}
        From: {}
        '''''.format(data['message'], data['email'])
        send_mail(data['subject'], message, '',['djangocontact44@gmail.com']) 

    return render(request,'contact.html',{})
     

def signup(request):
    if  request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'This username is already taken.')

                return redirect('home:signup')
            elif User.objects.filter( email = email).exists():
                messages.error(request, 'This email is already taken.')

                return redirect('home:signup')
            else:
                user = User.objects.create_user(
                    username = username,
                    email = email,
                    password = password,
                    )
                user.save()

                return redirect('/accounts/login')
        else:
            messages.error(request, 'Password does not match.')
            return redirect('home:signup')
    return render(request,'register.html')

def single(request):
    return render(request,'single-product.html')

class Search(BaseView):
    def get(self,request):
        if request.method == 'GET':

            query = request.GET['query']
            if query is None:
                return redirect('single/')
            self.views['search_product'] = Item.objects.filter(name__icontains = query)
        return render(request,'single-product.html',self.views)