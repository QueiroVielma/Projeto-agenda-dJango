from django.shortcuts import render
from contact.models import contact

def index (request):
    contacts= contact.objects.all()

    data={
        'contacts': contacts
    }

    return render(
        request,
        'contact/index.html',
        data
    )