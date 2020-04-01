from datetime import datetime

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView

from .forms import BlogForm
from .models import Blog


def home(request):
    return render(request, "blog/home.html")


def about(request):
    return render(request, "blog/about.html")


def contact(request):
    return render(request, "blog/contact.html")


class BlogListView(ListView):
    """Renders the home page, with a list of all messages."""

    model = Blog

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        return context


blog_list_view = BlogListView.as_view(
    queryset=Blog.objects.order_by("-added"),
    context_object_name="blog_list",
    template_name="blog/blog_list.html",
)


def blog_detail(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    return render(request, "blog/detail.html", {"post": post})


def blog_new(request):
    form = BlogForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=True)
            message.log_date = datetime.now()
            message.save()
            messages.success(request, "Added post")
            return redirect("blog:blog_list")

    else:
        return render(request, "blog/blog_new.html", {"form": form})


def blog_edit(request, pk):
    post = get_object_or_404(Blog, pk=pk)

    form = BlogForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        messages.success(request, "Edited post")
        return redirect("blog:blog_list")

    return render(request, "blog/form.html", {"post": post, "form": form})


def blog_delete(request, pk):
    post = get_object_or_404(Blog, pk=pk)

    if request.method == "POST":
        post.delete()
        messages.success(request, "Deleted post")
        return redirect("blog:blog_list")

    return render(request, "blog/delete.html", {"post": post})
