from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.db import transaction
from store.models import Product, Customer, Collection, Order, OrderItem
from tags.models import TaggedItem
# Create your views here.

def say_hello(request):


    order = Order(pk=1001)

    item = OrderItem()
    item.order = order
    item.product_id = 1
    item.unit_price = 10
    item.quantity = 5
    item.save()


    return render(request,'hello.html')