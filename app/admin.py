from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Contact 

# customizing admin 
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'info', 'gender', 'image', 'created_at') 
    list_editable = ('info',) 
    list_per_page = 10 # pagination 
    search_fields = ('name', 'gender', 'email', 'info', 'phone')
    list_filter = ('gender', 'created_at') 

# Register your models here.
admin.site.register(Contact, ContactAdmin)

# unregister 
admin.site.unregister(Group)