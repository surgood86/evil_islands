from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Content(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField('Text')
    datetime = models.DateTimeField(default=timezone.now)
    # author = models.CharField(max_length=100, null=True)
    blockquote = models.TextField(null=True)
    category = models.ManyToManyField(Category, related_name='content_articles')


class ContentImage(models.Model):
    content = models.ForeignKey(Content, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(null=True)

    def __str__(self):
        return f"Image for {self.content.title}"


class Gallery(models.Model):
    title = models.CharField(null=True, max_length=70)
    image = models.ImageField(null=True)
    categories = models.ManyToManyField(Category, related_name='galleries', blank=True)
    def __str__(self):
        return f"Image for {self.title}"
# class Comment(models.Model):
#    content = models.TextField(null=False)
#    author = models.ForeignKey(null=True, on_delete=models.SET_NULL, related_name='comments')
#    datetime = models.DateTimeField(auto_now_add=True)
#
#    def __str__(self):
#        return f"{self.author.username}: {self.content[:20]}"
#
