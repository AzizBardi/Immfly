import uuid

from django.db import models


class Content(models.Model):
    TYPE_CHOICES = [
        ('video', 'Video'),
        ('pdf', 'PDF'),
        ('text', 'Text')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    file = models.URLField(blank=True)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    slug = models.SlugField(unique=True, blank=False)



class SubtitleLanguage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    file = models.URLField(blank=True)
    content = models.ForeignKey('Content', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class AudioLanguage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    file = models.URLField(blank=True)
    content = models.ForeignKey('Content', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
