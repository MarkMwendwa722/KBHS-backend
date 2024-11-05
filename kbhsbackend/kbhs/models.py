from django.db import models
from django.core.validators import EmailValidator


# Create your models here.

class Assignment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=100, default="Unnamed Assignment")
    date = models.DateField(auto_now_add=True)
    form = models.CharField(max_length=40)
    file = models.FileField(upload_to='assignment/', default='assignment/default.pdf')
    
    def __str__(self):
        return f"{self.id} - {self.file}"
    
class Admissions(models.Model):
    name=models.CharField(max_length=100)
    admission_number=models.CharField(max_length=100,unique=True)
    date_of_admission=models.DateField(auto_now_add=True)
    form=models.CharField(max_length=100)
    
    
    def __str__(self):
        return f"{self.name} - {self.form}"
class ContactUs(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    
    def __str__(self):
        return f"Message from {self.name} - {self.message}"