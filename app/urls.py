from django.urls import path
from . import views
from . views import ContactList, ContactDetailView, ContactCreateView, ContactUpdateView

urlpatterns = [
    path('', ContactList.as_view(), name='home'), 
    path('detail/<int:pk>/', ContactDetailView.as_view(), name='single'),
    path('search/', views.search, name='search'),
    path('create', ContactCreateView.as_view(), name='create'),
    path('update/<int:pk>', ContactUpdateView.as_view(), name='update'), 
]
