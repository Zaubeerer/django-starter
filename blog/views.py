from datetime import datetime

from django.shortcuts import redirect, render

from .forms import BlogForm


def blog_list(request):
    return render(request, "blog/blog_list.html")


def blog_detail(request):
    pass


def blog_new(request):
    form = BlogForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
    else:
        return render(request, "blog/blog_new.html", {"form": form})


def blog_edit(request):
    pass


def blog_delete(request):
    pass
