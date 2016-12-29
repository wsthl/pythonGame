from __future__ import unicode_literals

import datetime 
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
@python_2_unicode_compatible
class NewUser(AbstractUser):    
    profile = models.CharField('profile', default='',max_length=256)

    def __str__(self):
        return self.username

@python_2_unicode_compatible
class Column(models.Model):
	name = models.CharField('column_name',max_length=256)
	intro = models.TextField('introduction',default='')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'column'
		verbose_name_plural = 'column'
		ordering = ['name']

@python_2_unicode_compatible
class Article(models.model):
	col