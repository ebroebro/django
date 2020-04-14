from django.db import models

# Create your models here.


class Community(models.Model):
    title=models.CharField(max_length=100)
    store_name=models.CharField(max_length=100)
    rank=models.IntegerField()
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)