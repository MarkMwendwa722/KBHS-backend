from rest_framework import serializers
from . models import *  

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        
        model= Assignment
        fields= '__all__'     
        
class AdmissionsSerializer(serializers.ModelSerializer):
    class Meta:
        
        model= Admissions
        fields= '__all__' 
        
class ContactUsSerilaizer(serializers.ModelSerializer):
    class Meta:
        
        model= ContactUs
        fields= '__all__' 
        
    
    
    
    
