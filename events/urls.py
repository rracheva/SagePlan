from django.conf.urls import *
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.conf.urls import url
from django.contrib import admin
from . import views
from .models import Event, Invite

urlpatterns = [
	# admin
	url(r'^admin/', include(admin.site.urls)),

	# General View
	url(r'^$', views.index, name='index'),

	#Detail View
	url(r'^(?P<event_id>[0-9]+)/$', views.detail, name='detail'),

	#Add Event
	url(r'^add_event/$', views.add_event, name='add_event'),


	#Invite Form
	url(r'^invite_view/$', views.invite_view, name='invite_view'),

	#Invite Logic
	url(r'^invite/$', views.invite, name='invite'),

	#User Form
	url(r'^signup/$', views.signup, name='signup'),

	#Add User
	url(r'^add_user/$', views.add_user, name='add_user'),

	#Search
	url(r'^search/$', views.search, name='search'),

	#Update
	url(r'^update/(?P<pk>\d+)/$', views.EventUpdate.as_view(model=Event, success_url='/'), name='update'),

]