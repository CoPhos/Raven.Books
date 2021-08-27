import uuid
from django.db import models
from django.utils import timezone
# Create your models here.

class Address(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default=uuid.uuid4,
        editable=False
    )
    street = models.CharField(max_length=255, null=False, blank=False)
    city = models.CharField(max_length=255, null=False, blank=False)
    state = models.CharField(max_length=255, null=False, blank=False)
    zipCode = models.CharField(max_length=5, null=False, blank=False)
    contact_phone = models.CharField(max_length=10, null=False, blank=False)
    extra_information = models.TextField(null=False, blank=False)

class Order(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default=uuid.uuid4,
        editable=False
    )
    order_date = models.DateTimeField(default=timezone.now, null=False, blank=False)
    sub_total = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False)
    shipping_cost = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False)
    total = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False)
    finished = models.BooleanField(default=False, null=False, blank=False)
    customer = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name="order_customer")
    book = models.ManyToManyField('books.Book', through='OrderBook', related_name="order_book")
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="order_address")
    # def __str__(self):
    #     return self.publisher_name
     
class OrderBook(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default=uuid.uuid4,
        editable=False
    )
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE, related_name="orderBook_book")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="orderBook_order")
    quantity = models.IntegerField(null=False, blank=False)
    price = models.DecimalField(max_digits=4, decimal_places=2,null=False, blank=False)