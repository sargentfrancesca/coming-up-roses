import json
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.core import serializers
from django.template import Context, loader, RequestContext
from client_site.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template

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

# class ContactView(generic.TemplateView):
#     template_name = 'contact.html'

#     def get_context_data(self, **kwargs):
#     	context = super(ContactView, self).get_context_data(**kwargs)
#         form_class = ContactForm
#         form = form_class
#     	return context

def contact(request):
    form_class = ContactForm

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            contact_phone = form.cleaned_data['contact_phone']
            content = form.cleaned_data['content']
            
            send_mail(contact_name, content, contact_email, ['contact@cominguproses.co.uk'])
            return redirect('success')
    
    return render(request, 'contact.html', {
        'form': form_class,
    })

def success(request):
    return HttpResponse('Success! Thank you for your message.')