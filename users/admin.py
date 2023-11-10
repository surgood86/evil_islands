from django.contrib import admin

from content.models import Content


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'datetime']
    list_filter = ('category')

    #def get_queryset(self, request):
    #    return super().get_queryset(request).filter(type='news')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'datetime']
    list_filter = ('category',)

    #def get_queryset(self, request):
    #    return super().get_queryset(request).filter(type='article')


admin.site.register(Content, NewsAdmin)
admin.site.unregister(Content)
admin.site.register(Content, ArticleAdmin)
