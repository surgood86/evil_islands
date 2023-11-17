from django.shortcuts import render
from django.views import generic
from .models import Content, Gallery, Category


class ContentListViews(generic.ListView):
    template_name = "home.html"
    context_object_name = "content_list"
    model = Content

    def get_queryset(self):
        return Content.objects.all()


class GalleryListView(generic.ListView):
    template_name = "gallery.html"
    context_object_name = "gallery_list"
    model = Gallery

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    # def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    context['news_list'] = Content.objects.filter(type='news')
    #    context['article_list'] = Content.objects.filter(type='article')
    #    context['video_contents'] = Content.objects.filter(video_url__isnull=False)
    #    return context


def base(request):
    return render(request, 'base.html')


def services(request):
    return render(request, 'services.html')


class ProjectDetailView(generic.ListView):
    model = Content
    template_name = 'project_detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def our_team(request):
    return render(request, 'our-team.html')


#def archives(request):
#    return render(request, 'archives.html')
#

#def grids(request):
#    return render(request, 'grids.html')
#

#def error_404(request):
#    return render(request, '404.html')
#

def contact(request):
    return render(request, 'contact.html')
