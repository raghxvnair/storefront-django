from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Customer, Collection, Order, OrderItem
from tags.models import TaggedItem
# Create your views here.

def say_hello(request):

    # collection = Collection.objects.get(pk=11)
    # collection.title = 'Games'
    # collection.featured_product_id = None
    # collection.save()

    # Collection.objects.create(title='Games', featured_product_id=None)
    # Collection.objects.filter(pk=11).update(featured_product_id=None)

    # Collection.objects.filter(pk__gt=5).delete()


    return render(request,'hello.html')