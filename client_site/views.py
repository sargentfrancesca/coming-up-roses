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
from client_site.models import Category, Treatment, Image

class AboutView(generic.TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
    	context = super(AboutView, self).get_context_data(**kwargs)
        context['images'] = Image.objects.filter(image_folder="photo_shoot").all()
    	return context

class TreatmentView(generic.TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
    	context = super(TreatmentView, self).get_context_data(**kwargs)
    	return context

class PolicyView(generic.TemplateView):
    template_name = 'policy.html'

    def get_context_data(self, **kwargs):
        context = super(PolicyView, self).get_context_data(**kwargs)
        return context

class PriceView(generic.TemplateView):
    template_name = 'prices.html'

    c = Category.objects.all()
    for x in c:
        print x.treatment_set.all()
    def get_context_data(self, **kwargs):
    	context = super(PriceView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
    	return context

def contact(request):
    form_class = ContactForm

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            contact_phone = str(form.cleaned_data['contact_phone'])
            content = form.cleaned_data['content']

            message = '{} [Phone: {}]'.format(content, contact_phone)
            print message
            
            try:
                send_mail(contact_name, message, contact_email, ['contact@cominguproses.co.uk'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    
    return render(request, 'contact.html', {
        'form': form_class,
    })

def success(request):
    return render(request, 'success.html')