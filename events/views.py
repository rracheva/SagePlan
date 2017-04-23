# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import redirect
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
	event_to_add.start_time = request.POST['event_start']
	event_to_add.end_time = request.POST['event_end']
	event_privacy = request.POST.get('event.privacy', False)
	print event_privacy
	event_to_add.privacy = True
	event_to_add.description = request.POST['event_description']
	event_to_add.location = request.POST['event_location']
	event_to_add.save()
	return redirect('/events/')
