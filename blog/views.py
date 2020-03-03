from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect

from .models import Blog
from .forms import BlogForm

from django.http import HttpResponse


def blog_list(request):
    posts = Blog.objects.all()
    return render(request, 'blog/list.html', {'posts': posts})

def blog_detail(request):


def blog_new(request):


def blog_edit(request):


def blog_delete(request):
