from django.db import models
from django.utils.translation import gettext_lazy as _


class Readers(models.Model):
    """Create an intacia for db readers"""

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    avatar = models.ImageField(
        _('Image your profile'),
        upload_to='./media',
        null=True,
        default='images/default.jpg'
    )
    email = models.CharField(max_length=80)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = (('view_post', 'Can view post'), ) # Dedicates a read-only permission for publications
        ordering = ('-created_at',) # sort by date creation

    def __str__(self):
        """Standardizes a representation for the readers model"""
        return f'"Reader": {self.name}, "Email": {self.email}'
