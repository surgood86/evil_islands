from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Content
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
        # Получаем контекст из суперкласса
        context = super().get_context_data(**kwargs)
        # Добавляем список категорий в контекст
        context['categories'] = Category.objects.all()
        return context
    # def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    context['news_list'] = Content.objects.filter(type='news')
    #    context['article_list'] = Content.objects.filter(type='article')
    #    context['video_contents'] = Content.objects.filter(video_url__isnull=False)
    #    return context


# class ContentDetailViews(generic.DetailView):
#    template_name = "articles.html"


def base(request):
    return render(request, 'base.html')


def services(request):
    return render(request, 'services.html')


# def projects_2(request):
#    return render(request, 'projects_2.html')
#

# class GalleryListViews:
# def projects_3(request):
#    return render(request, 'gallery.html')
#

def project_details(request):
    content = Content.objects.all().prefetch_related('images')  # Получить все объекты Content и связанные изображения
    return render(request, 'project_details.html', {'contents': content})

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
