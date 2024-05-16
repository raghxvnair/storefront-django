from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from store.models import Product, Customer, Collection, Order, OrderItem

# Create your views here.

def say_hello(request):
    # queryset = Order.objects.aggregate(count=Count('id'))
    # queryset = OrderItem.objects.filter(product__id=1).aggregate(sum=Sum('quantity'))
    # queryset = Order.objects.filter(customer__id=1).aggregate(count=Count('id'))
    queryset = Product.objects.filter(collection__id=3).aggregate(min=Min('unit_price'), max=Max('unit_price'), avg=Avg('unit_price'))


    return render(request,'hello.html', {'orders': queryset})