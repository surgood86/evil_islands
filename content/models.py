import os
from django.db import models


class Content(models.Model):
    TYPES = (
        ('news', 'News'),
        ('article', 'Article'),
    )

    type = models.CharField(max_length=10, choices=TYPES, default='article')
    title = models.TextField(null=False)
    content = models.TextField(null=False)
    image = models.ImageField(null=True)
    video_url = models.URLField(null=True, blank=True)
    #author = models.ForeignKey('users.User', null=True, on_delete=models.SET_NULL, related_name='contents')
    datetime = models.DateTimeField(auto_now_add=True)
    views_count = models.IntegerField(default=0)
    likes_count = models.IntegerField(default=0)

    def __str__(self):
        return os.path.basename(self.image.name) if self.image else self.title


#class Comment(models.Model):
#    content = models.TextField(null=False)
#    author = models.ForeignKey('users.User', null=True, on_delete=models.SET_NULL, related_name='comments')
#    datetime = models.DateTimeField(auto_now_add=True)
#
#    def __str__(self):
#        return f"{self.author.username}: {self.content[:20]}"
#