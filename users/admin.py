from django.contrib import admin
from .models import Content


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'datetime']
    list_filter = ('type',)

    def get_queryset(self, request):
        return super().get_queryset(request).filter(type='news')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'datetime']
    list_filter = ('type',)

    def get_queryset(self, request):
        return super().get_queryset(request).filter(type='article')


admin.site.register(Content, NewsAdmin)
admin.site.unregister(Content)
admin.site.register(Content, ArticleAdmin)
