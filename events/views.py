# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Event
from django.template import loader
import operator

from django.db.models import Q
from django.views.generic import ListView

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

def delete_event(request,event_id):
    query = Event.objects.get(pk=event_id)
    query.delete()
    return redirect('/events/')

class EventListView(ListView):

    model = Event

    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)
       # context['now'] = timezone.now()
        return context


class EventSearchListView(EventListView):
    """
    Display a event list page filtered by the search query.
    """
    #paginate_by = 10

    def get_queryset(self):
        result = super(EventSearchListView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.or_,
                       (Q(title__icontains=q) for q in query_list))
            )

        return result
        #return render_to_response('search/search_results.html',
                          # { 'query_string': query, 'found_entries': found_entries },
                          # context_instance=RequestContext(request))
