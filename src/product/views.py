from django.shortcuts import render, get_object_or_404
from .models import *
def detail(request, id):
    try:
        detail = Product.objects.get(pk=id);
    except Product.DoesNotExist:
        detail = None
    context= {"product": detail}
    return render(request, 'product/detail.html', context)