from django.db import models
from content.models import Category
from django.utils import timezone
from django_quill.fields import QuillField


class Blog(models.Model):
    content = QuillField()
    datetime = models.DateTimeField(default=timezone.now)
    category = models.ManyToManyField(Category, related_name='blog_articles')
