from django.db.models import Q  
from django.shortcuts import render, get_object_or_404, redirect
from contact.models import contact

def index (request):
    contacts= contact.objects.filter(show=True).order_by('-id')

    data={
        'contacts': contacts,
        'site_title': "contactos - "
    }

    return render(
        request,
        'contact/index.html',
        data
    )

def search (request):
    search_value= request.GET.get('q', '').strip()
    if(search== ' '):
        redirect('contact:index')
    contacts= contact.objects \
    .filter(show=True).filter(
        Q(first_name__icontains= search_value )|
        Q(Last_name__icontains= search_value )|
        Q(phone__icontains= search_value )|
        Q(email= search_value )
    )\
    .order_by('-id')


    data={
        'contacts': contacts,
        'site_title': "filter - "
    }

    return render(
        request,
        'contact/index.html',
        data
    )

def contact_met (request, contact_id):
    #single_contact= contact.objects.get(pk=contact_id)
    single_contact= get_object_or_404(contact, pk= contact_id, show=True )
    data={
        'contact': single_contact,
        'site_title':  f'{single_contact.first_name} {single_contact.Last_name} - '
    }

    return render(
        request,
        'contact/contact.html',
        data
    )