from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Customer, Collection, Order, OrderItem
from tags.models import TaggedItem
# Create your views here.

def say_hello(request):

    queryset = TaggedItem.objects.get_tags_for(Product,1)

    return render(request,'hello.html', {'orders': list(queryset)})