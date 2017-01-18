from __future__ import unicode_literals

from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    timeframe = models.ForeignKey('Timeframe', on_delete=models.CASCADE)
    is_closed = models.BooleanField()

class Category(models.Model):
    title = models.CharField(max_length=20, unique=True)

class Comment(models.Model):
    text = models.TextField(max_length=300)
    category = models.ForeignKey('Task', on_delete=models.CASCADE)

class Timeframe(models.Model):
    NOW = 0
    LATER = 1
    SOMEDAY = 2
    TIMEFRAMES = (
        (NOW, 'Now'),
        (LATER, 'Later'),
        (SOMEDAY, 'Someday'),
    )
    how_soon = models.IntegerField(choices=TIMEFRAMES, default=NOW)
