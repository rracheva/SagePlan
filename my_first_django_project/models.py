# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

# from django.db import models

# # Create your models here.

# class Event(models.Model):
# 	event_id = models.AutoField(primary_key=True, unique=True)
# 	title = models.CharField(max_length = 500)
# 	start_time = models.DateTimeField()
# 	end_time = models.DateTimeField()
# 	privacy = models.BooleanField()
# 	description = models.CharField(max_length = 1500)
# 	location = models.CharField(max_length = 500)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# class Event(models.Model):
# 	creator = models.ForeignKey(User, related_name="event_creator")
# 	event_id = models.AutoField(primary_key=True, unique=True)
# 	title = models.CharField(max_length = 500)
# 	start_time = models.DateTimeField()
# 	end_time = models.DateTimeField()
# 	privacy = models.BooleanField()
# 	description = models.CharField(max_length = 1500)
# 	location = models.CharField(max_length = 500)
# 
# 
# class Task(models.Model):
# 	creator = models.ForeignKey(User, related_name="task_creator")
# 	task_id = models.AutoField(primary_key=True, unique=True)
# 	title = models.CharField(max_length = 500)
# 	deadline = models.DateTimeField()
# 	description = models.CharField(max_length = 1500)
# 	typeOfTask = models.CharField(max_length = 500)
# 	urgency = models.IntegerField(default=100)
# 	completed = models.BooleanField()

# class Invite(models.Model):
# 	inviter = models.ForeignKey(User, related_name="inviter")
# 	invitee = models.ForeignKey(User, related_name="invitee")
# 	event = models.ForeignKey(Event, related_name="event_inv")
# 	accepted = models.BooleanField()

# class Share(models.Model):
# 	sharer = models.ForeignKey(User, related_name="sharer")
# 	sharee = models.ForeignKey(User, related_name="sharee")
# 	task = models.ForeignKey(Task, related_name="task_shr")

# class Depend(models.Model):
# 	depender = models.ForeignKey(Task, related_name="depender")
# 	dependee = models.ForeignKey(Task, related_name="dependee")





