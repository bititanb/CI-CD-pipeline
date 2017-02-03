from __future__ import unicode_literals
from django.template.defaultfilters import slugify

from django.db import models

def get_default_category():
    return Category.objects.get(id=1)

class Category(models.Model):
    title = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(editable=False)

    #def slug(self):
    #    return slugify(self.title)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

class Task(models.Model):
    title = models.CharField(max_length=20, unique=True)
    body = models.TextField(max_length=200, blank=True)
    slug = models.SlugField(editable=False)

    #import pudb; pudb.set_trace()
    category = models.ForeignKey('Category', on_delete=models.SET_DEFAULT, blank=False, default=get_default_category)

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


    def __unicode__(self):
        return self.title


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
