from django.db import models
from django.urls import reverse
from django.conf import settings
import misaka

from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField
User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts',
                             on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    message =  RichTextField(blank=True,null=True)
    message_html = models.TextField(editable=False)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    favourite = models.ManyToManyField(User, related_name='favorite', blank=True)
    pdf = models.FileField(null=True,blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)
    def total_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'message']

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='comments')
    name = models.CharField(max_length = 100)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)