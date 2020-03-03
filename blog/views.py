from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect

from .models import Blog
from .forms import BlogForm

from django.http import HttpResponse


def blog_list(request):
    return HttpResponse("Hello, world. You're at the blog_list index.")


def blog_detail(request):
    return HttpResponse("Hello, world. You're at the blog_detail index.")


def blog_new(request):
    return HttpResponse("Hello, world. You're at the blog_new index.")


def blog_edit(request):
    return HttpResponse("Hello, world. You're at the blog_edit index.")


def blog_delete(request):
    return HttpResponse("Hello, world. You're at the blog_delete index.")
