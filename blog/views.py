from django.shortcuts import render
from django.views import generic

from .models import Blog

from django.views import generic
from .models import Blog


class BlogListView(generic.ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = "blog_list"


    def get_context_data(self, **kwargs):
        """
        Получить дополнительный контекст для шаблона.
        """
        context = super().get_context_data(**kwargs)
        # Дополнительные переменные контекста можно добавить здесь, если это необходимо
        return context


class BlogDetailViews(generic.DetailView):
    template_name = 'blog_detail.html'
    context_object_name = "blog_details"
    model = Blog

    def get_queryset(self):
        return Blog.objects.all()
