# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Learning(models.Model):
    language=models.CharField(max_length=20)
    category=models.CharField(max_length=20)
    difficulty=models.CharField(max_length=20)
    words=models.CharField(max_length=20)

    def __str__(self):
        return self.language
