from django.shortcuts import render

# return home template 
def home(request):
    return render(request, 'index.html', {}) 
