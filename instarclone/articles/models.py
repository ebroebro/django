from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=20)
    content=models.TextField()
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users=models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Comment(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content=models.CharField(max_length=200)
    article=models.ForeignKey(Article, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)