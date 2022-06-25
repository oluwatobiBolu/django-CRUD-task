from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
from django.views import generic
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from .models import Post

#class PostList(generic.ListView):
    #model = Post

class PostListView(ListView):
    #queryset = Post.published.all()
    model = Post
    #paginate_by = 3
    #template_name = 'blog/post/list.html'

class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(CreateView):
    model = Post
    fields ="__all__"
    success_url  = reverse_lazy("blog:all")

class PostUpdateView(UpdateView):
    model = Post
    fields ="__all__"
    success_url  = reverse_lazy("blog:all")

class PostDeleteView(DeleteView):
    model = Post
    fields ="__all__"
    success_url  = reverse_lazy("blog:all")

