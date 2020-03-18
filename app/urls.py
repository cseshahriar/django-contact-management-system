from django.urls import path
from . import views
from . views import ContactList, ContactDetailView

urlpatterns = [
    path('', ContactList.as_view(), name='home'), 
    path('detail/<int:pk>/', ContactDetailView.as_view(), name='single'),
    path('search/', views.search, name='search'),
]
