from django.conf.urls import *
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
	# admin
	url(r'^admin/', include(admin.site.urls)),

	# General View
	url(r'^$', views.index, name='index'),

	#Detail View
	url(r'^(?P<event_id>[0-9]+)/$', views.detail, name='detail'),

	#Add Event
	url(r'^add_event/$', views.add_event, name='add_event'),

	url(r'^delete_event/(?P<event_id>[0-9]+)/$', views.delete_event, name='delete_event')

]