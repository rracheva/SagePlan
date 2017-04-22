# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Event(models.Model):
	event_id = models.AutoField(primary_key=True, unique=True)
	title = models.CharField(max_length = 500)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	privacy = models.BooleanField()
	description = models.CharField(max_length = 1500)
	location = models.CharField(max_length = 500)
