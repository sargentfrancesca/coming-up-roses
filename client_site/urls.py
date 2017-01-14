from django.conf.urls import patterns, url

from client_site import views

urlpatterns = patterns('',
	url(r"^about/", views.AboutView.as_view(), name="about"),
	)