from datetime import datetime

from django.shortcuts import redirect, render
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
    queryset=Blog.objects.order_by("-log_date")[
        :5
    ],  # :5 limits the results to the five most recent
    context_object_name="blog_list",
    template_name="blog/blog_list.html",
)


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
