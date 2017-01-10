from __future__ import unicode_literals

from django.db import models
from sorl.thumbnail import ImageField

class Plant(models.Model):
    norwegian_name = models.CharField(max_length=100)
    latin_name = models.CharField(max_length=100, blank=True)
    english_name = models.CharField(max_length=100, blank=True)
    norwegian_family = models.CharField(max_length=100)
    latin_family = models.CharField(max_length=100)
    english_family = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    def __unicode__(self):
        return self.norwegian_name

class Picture(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    date_taken = models.DateField()
    date_added = models.DateField(auto_now_add=True)
    picture = models.ImageField()
    def __unicode__(self):
        return self.plant.norwegian_name + str(self.pk)
