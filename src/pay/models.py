from django.db import models

# Create your models here.
from django.db import models

class Payment(models.Model):
    title = models.CharField(max_length=200)
    info = models.TextField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "To'lov turi"
        verbose_name_plural = "To'lov turlari"