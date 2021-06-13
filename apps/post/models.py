from django.db import models
from apps.authors.models import Authors

class Post(models.Model):
    title_post = models.CharField(
        'Title of post',
        max_length=200,
        blank=False,
        null=False,
    )
    description = models.CharField(
        'Descripton of post',
        max_length=150
    )
    post = models.TextField(
        max_length=500,
        blank=False,
        null=False,
        default='Post literals'
    )
    author = models.ForeignKey(
        Authors,
        related_name='posts',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return f'"Post title": {self.title_post}'