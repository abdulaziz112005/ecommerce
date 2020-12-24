from django.shortcuts import render, get_object_or_404
from .models import *

def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blog/blog.html', context)

def blog_info(request, id):
    try:
        view = Blog.objects.get(pk=id)
    except Blog.DoesNotExist:
        view = None
    context= {"view": view}
    return render(request, 'blog/blog_view.html', context)