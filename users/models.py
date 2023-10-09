from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    rating = models.IntegerField(default=0)
    author_name = models.CharField(max_length=50, null=True, blank=True)
    vk_link = models.URLField(null=True, blank=True)
    telegram_link = models.URLField(null=True, blank=True)
    instagram_link = models.URLField(null=True, blank=True)
    favourites = models.ManyToManyField('content.Content', related_name='favourited_by', blank=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username
