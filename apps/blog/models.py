from __future__ import unicode_literals

from django.utils import timezone
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank=True, null=True)
    datetime_created = models.DateTimeField()
    datetime_last_modified = models.DateTimeField()
    author = models.CharField(max_length=100, default='Анонім')
    language = models.CharField(choices=('EN', 'UA', 'RU'))
    text = models.TextField()

    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        if not self.id:
            self.datetime_created = timezone.now()
        self.datetime_last_modified = timezone.now()
        return super(Article, self).save(*args, **kwargs)
