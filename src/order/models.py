from django.db import models
from geo.models import Districts
from delivery.models import Delivery, Status
from pay.models import Payment
from staff.models import Staff
from product.models import Product
from django.contrib.auth.models import User

class Address(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=50)
    district = models.ForeignKey(Districts, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, editable=False)

    def __str__(self):
        return self.district + ", " + self.address

class Orders(models.Model):
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    delivery_time = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, editable=False)

class Products(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    cnt = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField(blank=True)
    sale_percent = models.IntegerField(blank=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, editable=False)