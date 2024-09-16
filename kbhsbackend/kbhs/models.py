from django.db import models
from django.core.validators import EmailValidator



# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=100) 
    email = models.EmailField(max_length=254, validators=[EmailValidator()])
    message= models.TextField()

    def __str__(self):
        return self.name + '|' + self.message




    
