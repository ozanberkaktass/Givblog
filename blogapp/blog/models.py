from time import time
from tkinter import CASCADE
import tkinter as tk
from django.db import models
from django.forms import IntegerField
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(null=False,blank=True,unique=True,db_index=True,editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blogs")
    description = RichTextField()
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    is_day= models.BooleanField(default=False)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
    data= models.DateTimeField(null=True,blank=True)
    pas= models.IntegerField(null=True)
    categories= models.ManyToManyField(Category,blank=True)
    post_type = models.ForeignKey("blog.navbar", null=True , related_name='post_type', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class navbar(models.Model):
    name=models.CharField(max_length=50)
    image = models.ImageField(upload_to="blogs", blank=True)
    slug = models.SlugField(null=True,blank=True,unique=True,db_index=True,editable=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

