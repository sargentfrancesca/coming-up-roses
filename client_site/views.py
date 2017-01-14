import json
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.core import serializers
from django.template import Context, loader, RequestContext

class AboutView(generic.TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
    	context = super(AboutView, self).get_context_data(**kwargs)
    	return context

class TreatmentView(generic.TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
    	context = super(TreatmentView, self).get_context_data(**kwargs)
    	return context

class PriceView(generic.TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
    	context = super(PriceView, self).get_context_data(**kwargs)
    	return context

class ContactView(generic.TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
    	context = super(ContactView, self).get_context_data(**kwargs)
    	return context