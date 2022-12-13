from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
      model = Post
      # ordering = 'categories'
      template_name = 'news.html'
      context_object_name = 'post'

class PostDetail(DetailView):
      model = Post
      template_name = 'post_id.html'
      context_object_name = 'post'

