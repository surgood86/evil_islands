from django.db import models
from content.models import Category
from django.utils import timezone
from django.utils.text import Truncator


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField('Text')
    datetime = models.DateTimeField(default=timezone.now)
    # author = models.CharField(max_length=100, null=True)
    blockquote = models.CharField(null=True)
    category = models.ManyToManyField(Category, related_name='blog_articles')

    def truncated_summary(self):
        return Truncator(self.content).chars(100, truncate='...')

    def get_first_image_url(self):
        first_image = self.images.first()
        if first_image and first_image.image:
            return first_image.image.url
        else:
            return None  # Или URL к изображению-заглушке


class BlogImage(models.Model):
    image = models.ImageField(null=True)
    content = models.ForeignKey(Blog, related_name='images', on_delete=models.CASCADE)

# class Comments(models.Model):
#    text = models.TextField
