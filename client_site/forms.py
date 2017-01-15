# make sure this is at the top if it isn't already
from django import forms

# our new form
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, label="Name *")
    contact_email = forms.EmailField(required=True, label="Email Address *")
    contact_phone = forms.CharField(label="Phone Number")
    content = forms.CharField(
        required=True,
        label="Query *",
        widget=forms.Textarea
    )