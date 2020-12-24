from django.db import models

# Create your models here.

class Staff(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, editable=False)

    def __str__(self):
        return self.last_name + " " + self.first_name
    class Meta:
        verbose_name = "Yetkazib beruvchi"
        verbose_name_plural = "Yetkazib beruvchilar"

