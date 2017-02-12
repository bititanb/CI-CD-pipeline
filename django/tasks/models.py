from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django import urls
from django.conf import settings
from current_user import get_current_user
from tasks import middleware

from django.db import models
from .middleware import *

#def get_default_category():
#    return Category.objects.get(id=1)

class Category(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=get_current_user, editable=False)
    #url = models.URLField(editable=False)

    #def slug(self):
    #    return slugify(self.title)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return urls.reverse('tasklist_by_category', kwargs={'pk': self.pk, 'slug': self.slug})

class Task(models.Model):
    title = models.CharField(max_length=20, editable=False)
    body = models.TextField(max_length=500, blank=False)
    slug = models.SlugField(editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=get_current_user, editable=False)

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)

    NOW = 0
    LATER = 1
    SOMEDAY = 2
    TIMEFRAMES = (
        (NOW, 'Now'),
        (LATER, 'Later'),
        (SOMEDAY, 'Someday'),
    )
    timeframe = models.IntegerField(choices=TIMEFRAMES)

    def save(self, *args, **kwargs):
        self.title = (self.body[:15]) if len(self.body) > 15 else self.body
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
