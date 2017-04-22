# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
from django.template import loader

# Create your views here.

def index(request):
	#return HttpResponse("<h1>Index Page</h1>")
	all_events = Event.objects.all()
	# html = ''
	# for event in all_events:
	# 	url = '/events/' + str(event.event_id) + '/'
	# 	html += '<a href="' + url + '">' + event.title + '</a><br>'
	# return HttpResponse(html)
	template = loader.get_template('events/index.html')
	context = {
		'all_events' : all_events,
	}
	return HttpResponse(template.render(context, request))

def detail(request, event_id):
	return HttpResponse("<h1>Event Detail for event " + str(event_id) + "</h1>")

def add_event(request):
	event_to_add = Event()
	event_title = request.POST['event_title']
	event_to_add.title = event_title
	event_to_add.start_time = '2017-12-25'
	event_to_add.end_time = '2017-12-25'
	event_to_add.privacy = True
	event_to_add.description = "Lit party. Everyone Roll THRUUUUU!!!"
	event_to_add.location = "Lawry A3"
	event_to_add.save()
	return HttpResponse("<h1>Saved Event " + event_title + " to Database!</h1>")
