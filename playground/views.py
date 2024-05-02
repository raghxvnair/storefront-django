from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product, Customer, Collection, Order, OrderItem

# Create your views here.

def say_hello(request):
    # customers = Customer.objects.filter(email__endswith='.com')
    # print(customers)
    # collection = Collection.objects.filter(featured_product__isnull=True)
    # print(collection)
    # product = Product.objects.filter(inventory__lt=10)
    # print(product)
    # order = Order.objects.filter(customer__id=1)
    # print(order)
    queryset= OrderItem.objects.filter(product__collection__id=3)
    print(queryset)

    return render(request,'hello.html', {'products': list(queryset)})