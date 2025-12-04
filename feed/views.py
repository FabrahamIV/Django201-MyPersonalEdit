from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .models import Post
# Create your views here.

class HomePage(ListView):
    http_method_names = ['get']
    template_name = "home.html"
    model = Post
    context_object_name = "posts"
    queryset = Post.objects.all().order_by('-created_at')[0:30]


class PostDetailView(DetailView):
    http_method_names = ['get']
    template_name = "includes/post_detail.html"
    model = Post
    context_object_name = "post"


class CreatedNewPost(CreateView):
    http_method_names = ['get', 'post']
    template_name = "includes/post_detail.html"
    model = Post
    context_object_name = "post"
