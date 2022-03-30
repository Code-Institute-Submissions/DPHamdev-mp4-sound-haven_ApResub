from django.shortcuts import render

# Create your views here.

def contact(request):
    """ Contact Us Page """

    return render(request, 'contact/contact.html')
