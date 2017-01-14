from django.conf.urls import patterns, url

from client_site import views
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
	url(r"^about/", views.AboutView.as_view(), name="about"),
	)

from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
