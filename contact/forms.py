from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Contact


class ContactForm(forms.ModelForm):
    """ Contact Form """

    class Meta:
        """ Specify model, fields, and label """
        model = Contact
        fields = ('name', 'email', 'order_number', 'message')
        labels = {
            'name': _('Full Name'),
            'email': _('Email Address'),
            'order_number': _('Order Number'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)