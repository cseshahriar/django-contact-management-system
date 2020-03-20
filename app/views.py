from django.shortcuts import render, get_object_or_404, redirect   
from django.views.generic import ListView, DetailView 
from app.models import Contact
from django.db.models import Q 
from django.views.generic.edit import CreateView, UpdateView, DeleteView  
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required # for function base views 
from django.urls import reverse_lazy

# class base view 
class ContactList(LoginRequiredMixin, ListView):  
    template_name = 'index.html'
    model = Contact 
    context_object_name = 'contacts'  
    # return loggein user contacts
    def get_queryset(self):
        contacts = super().get_queryset()
        return contacts.filter(manager=self.request.user)

class ContactDetailView(DetailView):
    template_name = 'detail.html'
    model = Contact 
    context_object_name = 'contact'

@login_required
def search(request):
    if request.GET:
        search_term = request.GET['search_term']
        search_results = Contact.objects.filter(
            Q(name__icontains=search_term) or 
            Q(email__icontains=search_term) or 
            Q(phone__icontains=search_term) or
            Q(info__iexcept=search_term) 
        )  
        context = {  
            'search_term': search_term,
            'contacts': search_results 
        }   
        return render(request, 'search.html', context)  
    else:
        return redirect('home') # url name 


class ContactCreateView(CreateView):
    model = Contact 
    template_name = 'create.html'
    fields = ['name', 'email', 'phone', 'info', 'gender', 'image']
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.manager = self.request.user
        instance.save()
        return redirect('home')   


class ContactUpdateView(UpdateView):
    model = Contact 
    template_name = 'update.html'
    fields = ['name', 'email', 'phone', 'info', 'gender', 'image']
    
    def form_valid(self, form):
        instance = form.save()
        return redirect('single', instance.pk)  


class ContactDeleteView(DeleteView): 
    model = Contact 
    template_name = 'delete.html'
    success_url = '/'


class SignUpView(CreateView):
     form_class = UserCreationForm
     template_name = 'registration/signup.html'
     success_url = reverse_lazy('home')  