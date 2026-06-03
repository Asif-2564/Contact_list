from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy

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

class ContactCreateView(CreateView):
    model = Contacts
    template_name = 'contacts/contact_new.html'
    fields = ['author','first_name','last_name','phone_number','email']
    context_object_name = 'contacts'
    
class ContactUpdateView(UpdateView):
    model = Contacts
    template_name = 'contacts/contact_edit.html'
    fields = ['first_name','last_name','phone_number','email']
    context_object_name = 'contacts'

class ContactDeleteView(DeleteView):
    model = Contacts
    template_name = 'contacts/contact_delete.html'
    success_url = reverse_lazy('home')