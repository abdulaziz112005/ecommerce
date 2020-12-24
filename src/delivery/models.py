from django.db import models

# Create your models here.
class Delivery(models.Model):
    title = models.CharField(max_length=200)
    info = models.TextField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, editable=False)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Yetkazib berish turi"
        verbose_name_plural = "Yetkazib berish turilari"

class Status(models.Model):
    title = models.CharField(max_length=200)
    info = models.TextField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, editable=False)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Buyurtma holat"
        verbose_name_plural = "Buyurtma holat"
