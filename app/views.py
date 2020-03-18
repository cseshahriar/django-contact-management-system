from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from app.models import Contact

# class base view 
class ContactList(ListView):
    template_name = 'index.html'
    model = Contact 
    context_object_name = 'contacts'  

class ContactDetailView(DetailView):
    template_name = 'detail.html'
    model = Contact 
    context_object_name = 'contact'