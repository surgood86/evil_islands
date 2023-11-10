from django.contrib import admin
from .models import Blog, BlogImage


class BlogImageInline(admin.TabularInline):  # или admin.StackedInline
    model = BlogImage
    extra = 1  # Количество пустых форм, отображаемых по умолчанию


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'datetime', 'content')
    inlines = [BlogImageInline]
