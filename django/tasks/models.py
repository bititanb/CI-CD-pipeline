from __future__ import unicode_literals
from django.template.defaultfilters import slugify

from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=20, unique=True)
    slug = models.SlugField()

    #def slug(self):
    #    return slugify(self.title)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

class Task(models.Model):
    title = models.CharField(max_length=20, unique=True)
    body = models.TextField(max_length=200)
    is_closed = models.BooleanField()
    slug = models.SlugField()

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

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Task, self).save(*args, **kwargs)


#class Comment(models.Model):
#    text = models.TextField(max_length=300)
#    category = models.ForeignKey(Task, on_delete=models.CASCADE)

#class Recipe(models.Model):
#    title = models.CharField(max_length=255)
#    description = models.TextField()
#
#
#class Ingredient(models.Model):
#    recipe = models.ForeignKey(Recipe)
#    description = models.CharField(max_length=255)
#
#
#class Instruction(models.Model):
#    recipe = models.ForeignKey(Recipe)
#    number = models.PositiveSmallIntegerField()
#    description = models.TextField()
