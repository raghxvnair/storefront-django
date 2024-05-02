from django.db import models

# Create your models here.
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey(
        'Product', on_delete=models.SET_NULL, null=True, 
        related_name='+' 
    )

class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(
        Collection, on_delete=models.PROTECT
    )
    promotion = models.ManyToManyField(Promotion)


class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = {
        MEMBERSHIP_BRONZE : 'Bronze',
        MEMBERSHIP_SILVER :'Silver',
        MEMBERSHIP_GOLD : 'Gold'
    }

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    birth_date = models.DateField(null=True)
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, 
        default=MEMBERSHIP_BRONZE
    )
    

class Order(models.Model):
    PENDING_STATE = 'P'
    COMPLETED_STATE = 'C'
    FAILED_STATE = 'F'

    STATUS_CHOICES = {
        PENDING_STATE : 'Pending',
        COMPLETED_STATE :'Completed',
        FAILED_STATE : 'Failed'
    }

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=STATUS_CHOICES,
        default=PENDING_STATE
    )
    customer = models.ForeignKey(
        Customer, on_delete=models.PROTECT
        )


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.PROTECT
        )
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT
        )
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE
    )
    quantity = models.PositiveSmallIntegerField()


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=20, null=True)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE
    )