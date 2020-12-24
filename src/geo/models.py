from django.db import models

# Create your models here.
class Regions(models.Model):
    title = models.CharField(max_length=200)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Viloyat"
        verbose_name_plural = "Viloyatlar"

class Districts(models.Model):
    region = models.ForeignKey(Regions, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Tuman"
        verbose_name_plural = "Tumanlar"