import uuid

from django.db import models

class Channel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    language = models.CharField(max_length=50)
    picture = models.URLField(blank=True)
    contents = models.ManyToManyField('Content', blank=True)
    subchannels = models.ManyToManyField('self', blank=True, symmetrical=False)
    slug = models.SlugField(unique=True, blank=False)
