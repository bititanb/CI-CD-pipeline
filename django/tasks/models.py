from __future__ import unicode_literals
from django.template.defaultfilters import slugify

from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=20, unique=True)

    #def slug(self):
    #    return slugify(self.title)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

class Task(models.Model):
    title = models.CharField(max_length=200)
    is_closed = models.BooleanField()

    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    NOW = 0
    LATER = 1
    SOMEDAY = 2
    TIMEFRAMES = (
        (NOW, 'Now'),
        (LATER, 'Later'),
        (SOMEDAY, 'Someday'),
    )
    timeframe = models.IntegerField(choices=TIMEFRAMES, default=NOW)


#class Comment(models.Model):
#    text = models.TextField(max_length=300)
#    category = models.ForeignKey(Task, on_delete=models.CASCADE)
