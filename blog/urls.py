from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.blog_list_view, name="blog_list"),
    path("home", views.home, name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("blog_list", views.blog_list_view, name="blog_list"),
    path("blog_detail", views.blog_detail, name="blog_detail"),
    path("blog_new", views.blog_new, name="blog_new"),
    path("<int:pk>", views.blog_detail, name="blog_detail"),
    path("new", views.blog_new, name="blog_new"),
    # path("edit/<int:pk>", views.blog_edit, name="blog_edit"),
    # path("delete/<int:pk>", views.blog_delete, name="blog_delete"),
]
