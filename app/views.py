from django.shortcuts import render
from .models import Contact

# return home template 
def home(request):
    context = {
        'contacts': Contact.objects.all() 
    }
    return render(request, 'index.html', context) 
