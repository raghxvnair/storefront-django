from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.db import transaction
from store.models import Product, Customer, Collection, Order, OrderItem
from tags.models import TaggedItem
# Create your views here.

def say_hello(request):


    queryset = Product.objects.raw('SELECT * FROM store_product')


    return render(request,'hello.html', {'orders': list(queryset)})