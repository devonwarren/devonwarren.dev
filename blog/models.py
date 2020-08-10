from django.db import models
from autoslug import AutoSlugField
from martor.models import MartorField


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(populate_from='title', max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = MartorField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
