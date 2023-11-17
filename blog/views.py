from django.views import generic
from .models import Blog


class BlogListView(generic.ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = "blog_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    context_object_name = "blog_detail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
