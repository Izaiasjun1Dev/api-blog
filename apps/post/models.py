from django.db import models
from apps.authors.models import Authors

class Post(models.Model):
    """Initializes a valid publication model in the database"""

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

    class Meta: # Sort by creation date
        ordering = ('-created_at', )

    def __str__(self):
        """Creates a representative model 
        of a model with the title"""

        return f'"Post title": {self.title_post}'