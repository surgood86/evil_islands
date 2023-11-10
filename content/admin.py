from django.contrib import admin
from .models import Content, Category, ContentImage, Gallery


# Этот класс должен быть объявлен перед его использованием в ContentAdmin
class ContentImageInline(admin.TabularInline):  # или admin.StackedInline
    model = ContentImage
    extra = 1  # Количество пустых форм, отображаемых по умолчанию


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'datetime', 'blockquote')  # Поля, которые будут отображаться в списке
    inlines = [ContentImageInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Используем list_display вместо category


@admin.register(ContentImage)
class ContentImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'get_categories')

    def get_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    get_categories.short_description = 'Categories'
