import json
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.core import serializers
from django.template import Context, loader, RequestContext
from client_site.forms import ContactForm
from django.core.mail import EmailMessage
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

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the 
            # contact information
            template = get_template('contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Coming Up Roses Queries" +'',
                ['contact@cominguproses.co.uk'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            
            return redirect('contact')
    
    return render(request, 'contact.html', {
        'form': form_class,
    })