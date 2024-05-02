from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from store.models import Product, Customer, Collection, Order, OrderItem

# Create your views here.

def say_hello(request):

    # inventory = price 
    queryset = Product.objects.filter(inventory = F("unit_price"))
    return render(request,'hello.html', {'products': list(queryset)})