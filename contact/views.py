from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ContactForm
from .models import Contact


def contact(request):
    """ Contact Us Page """

    contact = get_object_or_404(Contact)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Contact Form submitted. Thank you!'
            )
            return redirect('contact')
    else:
        form = ContactForm()

    context = {
        'form': form,
    }

    return render(request, 'contact/contact.html', context)
