# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from events.models import Event, Invite
from django.template import loader

# Create your views here.

def home(request):
	#return HttpResponse("<h1>Index Page</h1>")
    if request.user.is_authenticated:
	   hosted_events = Event.objects.filter(creator=request.user)
	   invited_to = Invite.objects.filter(invitee=request.user)
	   invited_to_ids = invited_to.values_list('event_id', flat=True)
	   invited_events = []
	   for event in Event.objects.all():
		    print event.event_id
		    if event.event_id in invited_to_ids:
			   invited_events.append(event)


	# html = ''
	# for event in all_events:
	# 	url = '/events/' + str(event.event_id) + '/'
	# 	html += '<a href="' + url + '">' + event.title + '</a><br>'
	# return HttpResponse(html)
    	template = loader.get_template('home.html')
    	context = {
    		'all_events' : Event.objects.all(),
    		'hosted_events' : hosted_events,
    		'invited_events' : invited_events, 
    	}
	return HttpResponse(template.render(context))











