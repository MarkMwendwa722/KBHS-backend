from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import *
from . serializers import *

# Create your views here.
@api_view(['GET'])
def Home(request):
    print('johnson ')
    return Response({'Johnson Test Area!!'})

# @api_view(['GET'])
# def Contact_us(request):
#     contact = ContactUs.objects.all()
#     serializer = ContactUsSerializer(contact, many=True)
#     return Response(serializer.data)

    



