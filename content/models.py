from django.db import models
from django.utils import timezone
from django_quill.fields import QuillField


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Content(models.Model):
    content = QuillField()
    datetime = models.DateTimeField(default=timezone.now)
    category = models.ManyToManyField(Category, related_name='content_articles')


class Gallery(models.Model):
    title = models.CharField(null=True, max_length=70)
    image = models.ImageField(null=True)
    categories = models.ManyToManyField(Category, related_name='galleries', blank=True)

    def __str__(self):
        return f"Image for {self.title}"
