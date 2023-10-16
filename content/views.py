from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Content

from django.views import generic
from .models import Content


class ContentListViews(generic.ListView):
    template_name = "home.html"
    context_object_name = "content_list"

    def get_queryset(self):
        return Content.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_list'] = Content.objects.filter(type='news')
        context['article_list'] = Content.objects.filter(type='article')
        context['video_contents'] = Content.objects.filter(video_url__isnull=False)
        return context


from django.shortcuts import render

def base(request):
    return render(request, 'base.html')

def services(request):
    return render(request, 'services.html')

def projects_2(request):
    return render(request, 'projects-2.html')

def projects_3(request):
    return render(request, 'projects-3.html')

def project_details(request):
    return render(request, 'project-details.html')

def blog(request):
    return render(request, 'blog.html')

def blog_single(request):
    return render(request, 'blog-single.html')

def our_team(request):
    return render(request, 'our-team.html')

def archives(request):
    return render(request, 'archives.html')

def grids(request):
    return render(request, 'grids.html')

def error_404(request):
    return render(request, '404.html')

def contact(request):
    return render(request, 'contact.html')


