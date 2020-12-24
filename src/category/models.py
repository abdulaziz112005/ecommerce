from django.db import models
from django.template.defaultfilters import slugify

class Category(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(max_length=200, upload_to='categories')
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, editable=False)

    def __str__(self):
        return self.name
    def slug(self):
        return slugify(self.name)
    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"


class Brend(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    logo = models.ImageField(max_length=200, upload_to='brends')
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, editable=False)

    def slug(self):
        return slugify(self.name)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Brendlar"
        verbose_name_plural = "Brendlar"

class Model(models.Model):
    name = models.CharField(max_length=200)
    brend = models.ForeignKey(Brend, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, editable=False)
    def __str__(self):
        return self.name

    def slug(self):
        return slugify(self.name)

    class Meta:
        verbose_name = "Modellar"
        verbose_name_plural = "Modellar"