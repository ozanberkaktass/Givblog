from unicodedata import category
from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import Blog, Category,navbar

def index(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True,is_home=True),
    }
    return render(request, "blog/index.html", context)

def blogs(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True),
    }
    return render(request, "blog/blogs.html", context)

def csharp(request, slug):
    context = {
        "blogs": Blog.objects.filter(is_active=True,post_type__slug=slug),
    }
    return render(request, "blog/blog.html", context)

def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, "blog/blog-details.html", {
        "blog": blog,
        "selected_category":slug
    })

def blogs_by_category(request, slug):
    context = {
        "blogs":Category.objects.get(slug=slug).blog_set.filter(is_active=True),
        # "blogs": Blog.objects.filter(is_active=True,category__slug=slug),
        "selected_category":slug
    }
    return render(request, "blog/blogs.html", context)