from .models import Post
from django.views.generic import ListView, DetailView

# Blogs list on home page
class BlogListView(ListView):
    model = Post
    template_name = "home.html"


# Individual blog page.
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'