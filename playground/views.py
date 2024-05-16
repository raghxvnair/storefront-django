from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from store.models import Product, Customer, Collection, Order, OrderItem

# Create your views here.

def say_hello(request):

    # inventory = price 
    products = OrderItem.objects.values('product_id').distinct()
    queryset = Product.objects.filter(id__in=products).order_by('title')
    return render(request,'hello.html', {'products': list(queryset)})