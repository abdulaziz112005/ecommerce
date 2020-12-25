from django.db import models
from category.models import Brend, Model, Category

class Product(models.Model):
    name = models.CharField(max_length=200)
    product_code = models.CharField(max_length=200, unique=True)
    info = models.TextField(max_length=400)
    warranty = models.TextField(max_length=200)
    view_count = models.IntegerField(default=0, blank=True,editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brend = models.ForeignKey(Brend, on_delete=models.SET_NULL, null=True,blank=True)
    model = models.ForeignKey(Model, on_delete=models.SET_NULL, null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, editable=False)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Produkt"
        verbose_name_plural = "Produktlar"

class Items(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField(blank=True)
    sale_percent = models.IntegerField(blank=True, default=0)
    cnt = models.IntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, editable=False)

    class Meta:
        verbose_name = "Produkt turlari"
        verbose_name_plural = "Produkt  turlari"

class Attributes(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, editable=False)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Attributlar"
        verbose_name_plural = "Attributlar"

class Values(models.Model):
    name = models.CharField(max_length=200)
    attribute = models.ForeignKey(Attributes, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, editable=False)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Qiymatlar"
        verbose_name_plural = "Qiymatlar"

class ItemValue(models.Model):
    value = models.ForeignKey(Values, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, editable=False)

class Photo(models.Model):
    photo = models.ImageField(max_length=200, upload_to='products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, editable=False)