# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Event(models.Model):
	creator = models.ForeignKey(User)
	event_id = models.AutoField(primary_key=True, unique=True)
	title = models.CharField(max_length = 500)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	privacy = models.BooleanField()
	description = models.CharField(max_length = 1500)
	location = models.CharField(max_length = 500)


class Task(models.Model):
	creator = models.ForeignKey(User)
	task_id = models.AutoField(primary_key=True, unique=True)
	title = models.CharField(max_length = 500)
	deadline = models.DateTimeField()
	description = models.CharField(max_length = 1500)
	typeOfTask = models.CharField(max_length = 500)
	urgency = models.IntegerField(default=100)
	completed = models.BooleanField()

class Invite(models.Model):
	inviter = models.ForeignKey(User)
	invitee = models.ForeignKey(User)
	event = models.ForeignKey(Event)
	accepted = models.BooleanField()

class Share(models.Model):
	inviter = models.ForeignKey(User)
	invitee = models.ForeignKey(User)
	task = models.ForeignKey(Task)

class Depend(models.Model):
	depender = models.ForeignKey(Task)
	dependee = models.ForeignKey(Task)




