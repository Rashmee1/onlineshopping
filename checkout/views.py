from django.shortcuts import render
from .models import *
from home.models import Item 
from home.views import *
from django.contrib.auth.decorators import login_required




# Create your views here.

class CheckoutView(BaseView):
    def get(self,request):
        self.views['checkouts'] = Checkoutform.objects.all()
        self.views['total_cart'] = Totalcart.objects.all()
      
        return render(request,'checkout.html',self.views)

@login_required
def checkoutform(request):
    if  request.method =='POST':
        Ordered_by = request.POST['Ordered_by']
        country = request.POST['country']
        address = request.POST['address']
        emailaddress = request.POST['emailaddress']
        phone = request.POST['phone']
        user = Checkoutform.objects.create_user(

            Ordered_by = Ordered_by,
            country = country,
            address = address,
            emailaddress = emailaddress,
            phone = phone,
            )
        user.save()

        return redirect('checkout:checkoutform')

    return redirect('checkout:checkoutform')







def total_cart(request):
    cart= Cart.objects.get(slug=slug).cart
    total=0
    for cart in carts:
        total = total + cart.sub_total
    
    cart.save()
    return redirect('checkout:Totalcart')
       
    
        