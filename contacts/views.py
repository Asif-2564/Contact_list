from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Contacts
# Create your views here.

class ContactListView(ListView):
    model = Contacts
    template_name = 'contacts/home.html'
    context_object_name = 'contacts'

class ContactDetailView(DetailView):
    model = Contacts
    template_name = 'contacts/contact_detail.html'
    context_object_name = 'contacts'