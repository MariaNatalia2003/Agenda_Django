from django.shortcuts import render, get_object_or_404
from contact.models import Contact
from django.core.paginator import Paginator

from contact.forms import ContactForm

# Create your views here.
def create(request):
    if request.method == 'POST':
        context = {
            'form': ContactForm(request.POST)
        }

        return render(
            request,
            'contact/create.html',
            context,
        )
    context = {
        'form': ContactForm(request.POST)
    }

    return render(
        request,
        'contact/create.html',
        context,
    )
