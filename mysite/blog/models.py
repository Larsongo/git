from __future__ import unicode_literals

from django.db import models
class User(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __unicode__(self):
        return self.name
