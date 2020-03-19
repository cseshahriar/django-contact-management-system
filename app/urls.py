from django.urls import path
from . views import ContactList, ContactDetailView, ContactCreateView, ContactUpdateView, ContactDeleteView, SignUpView, search

urlpatterns = [
    path('', ContactList.as_view(), name='home'), 
    path('detail/<int:pk>/', ContactDetailView.as_view(), name='single'),
    path('search/', search, name='search'),
    path('create', ContactCreateView.as_view(), name='create'),
    path('update/<int:pk>', ContactUpdateView.as_view(), name='update'), 
    path('delete/<int:pk>', ContactDeleteView.as_view(), name='delete'), 
    path('signup/', SignUpView.as_view(), name='signup'),
]
