# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Event, Invite
from django.contrib.auth.models import User
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

def signup(request):
	#return HttpResponse("<h1>Index Page</h1>")
	all_users = User.objects.all()
	# html = ''
	# for event in all_events:
	# 	url = '/events/' + str(event.event_id) + '/'
	# 	html += '<a href="' + url + '">' + event.title + '</a><br>'
	# return HttpResponse(html)
	template = loader.get_template('events/signup.html')
	context = {
		'all_users' : all_users,
	}
	return HttpResponse(template.render(context, request))

def invite_view(request):
	#return HttpResponse("<h1>Index Page</h1>")
	my_events = Event.objects.filter(creator=request.user)
	# html = ''
	# for event in all_events:
	# 	url = '/events/' + str(event.event_id) + '/'
	# 	html += '<a href="' + url + '">' + event.title + '</a><br>'
	# return HttpResponse(html)
	template = loader.get_template('events/invite.html')
	context = {
		'my_events' : my_events,
	}
	return HttpResponse(template.render(context, request))

def detail(request, event_id):
	event = Event.objects.get(event_id=event_id)
	print event.title
	template = loader.get_template('events/event_detail.html')
	context = {
		'event' : event,
	}
	return HttpResponse(template.render(context, request))

def add_event(request):
	event_to_add = Event()
	event_to_add.creator = request.user
	event_title = request.POST['event_title']
	event_to_add.title = event_title
	event_to_add.start_time = request.POST['event_start']
	event_to_add.end_time = request.POST['event_end']
	event_to_add.privacy = request.POST.get('event.privacy', False)
	event_to_add.description = request.POST['event_description']
	event_to_add.location = request.POST['event_location']
	event_to_add.save()

	return redirect('/')

def add_user(request):
	username = request.POST.get('username')
	email = request.POST.get('email')
	password = request.POST.get('password')
	print username
	print email
	print password
	user_to_add = User.objects.create_user(username, email, password)
	user_to_add.save()
	return redirect('/')


def invite(request):
	invite_to_add = Invite()
	inviter = request.user
	all_users = User.objects.all()
	invitee_form = request.POST.get('invitee')
	invitee = all_users.filter(username=invitee_form)
	event = Event.objects.filter(event_id=request.POST.get('event_inv'))
	invite_to_add.invitee = invitee[0]
	invite_to_add.inviter = inviter
	invite_to_add.event = event[0]
	invite_to_add.accepted = False
	invite_to_add.save()
	return redirect('/')

def search(request):
	search = request.POST.get('search')
	print search
	print "-----"
	all_events = Event.objects.all()
	hosted_events = Event.objects.filter(creator=request.user, title=search)
	public_events = Event.objects.filter(privacy=False, title=search)
	invited_to = Invite.objects.filter(invitee=request.user)
	invited_to_ids = invited_to.values_list('event_id', flat=True)
	invited_events = []
	for event in all_events:
		print event.title
		if event.event_id in invited_to_ids and event.title==search:
			invited_events.append(event)

	template = loader.get_template('events/search_results.html')
	context = {
		'public_events' : public_events,
		'hosted_events' : hosted_events,
		'invited_events' : invited_events, 
	}
	return HttpResponse(template.render(context, request))











