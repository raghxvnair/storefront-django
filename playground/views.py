from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product, Customer, Collection, Order, OrderItem

# Create your views here.

def say_hello(request):

    # inventory < 10 AND price < 20
    # queryset = Product.objects.filter(inventory__lt=10, unit_price__lt=20)
    queryset = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)
    return render(request,'hello.html', {'products': list(queryset)})