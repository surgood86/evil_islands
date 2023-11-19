from django.contrib import admin
from .models import Content, Category, Gallery
from django.utils.translation import gettext_lazy as _
from django.utils import formats


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')


class ContentAdmin(admin.ModelAdmin):
    list_display = ('formatted_datetime', 'display_categories')
    fields = ('datetime', 'category', 'content')

    def formatted_datetime(self, obj):
        return formats.date_format(obj.datetime, format='d F Y', use_l10n=True)

    formatted_datetime.short_description = _('Дата и время')

    def display_categories(self, obj):
        return ', '.join([category.name for category in obj.category.all()])

    display_categories.short_description = _('Категории')


admin.site.register(Content, ContentAdmin)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
