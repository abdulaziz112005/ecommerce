from django.db import models
from django.template.defaultfilters import slugify


class Blog(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(max_length=200, upload_to='blogs', null=True)
    info = models.TextField(max_length=400)
    created_at = models.DateTimeField(auto_now=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name

    def slug(self):
        return slugify(self.name)

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"


