from django.db import models
from django.contrib.auth.models import User

# models

# article model
class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(
        to=User, 
        on_delete=models.PROTECT,
        related_name='articles',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"${self.title}"
