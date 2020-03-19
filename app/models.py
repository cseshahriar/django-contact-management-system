from django.db import models
from django.utils.timezone import datetime

# contact model 
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    info = models.CharField(max_length=30)
    gender = models.CharField(max_length=50, choices=(
        ('male', 'Male'),
        ('female', 'Female')
    ))
    image = models.ImageField(upload_to='images/', blank=True)
    created_at = models.DateTimeField(default=datetime.now)    

    def __str__(self):
        return self.name  
    
    class Meta():
        ordering= ['-id'] # desc order  
     
    