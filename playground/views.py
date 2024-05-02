from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from store.models import Product, Customer, Collection, Order, OrderItem

# Create your views here.

def say_hello(request):

    # inventory < 10 OR price < 20
    queryset = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    return render(request,'hello.html', {'products': list(queryset)})