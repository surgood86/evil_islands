from django.contrib import admin
from .models import Content


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'datetime', 'video_url')  # Поля, которые будут отображаться в списке
    #search_fields = 'title'  # Поля, по которым можно будет проводить поиск
    #list_filter = 'datetime'  # Поля, по которым можно будет фильтровать

# Регистрация модели
# admin.site.register(Content, ContentAdmin)  # Если без кастомизации, то просто admin.site.register(Content)
