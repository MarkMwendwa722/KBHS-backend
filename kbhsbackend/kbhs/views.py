from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import redirect
from . serializers import *
from . models import *


@api_view(['POST'])
def create_assignment(request):
    if request.method =='POST':
        serializer= AssignmentSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Assignment submitted successfully"})
        return Response(serializer.errors)
    
@api_view(['GET'])
def list_assignment(request):
    if request.method =='GET':
        assignments = Assignment.objects.all()
        serializer= AssignmentSerializer(assignments, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def update_assignment(request, id):
    try:
        assignment = Assignment.objects.get(id=id)
    except Assignment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = AssignmentSerializer(assignment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['DELETE'])
def delete_assignment(request, id):
    try:
        assignment = Assignment.objects.get(id=id)
    except Assignment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        assignment.delete()
        return Response({"message": "Assignment deleted successfully"})
    
@api_view(['GET'])
def redirect_to_nairobi(request):
  
    latitude = '-1.286389'
    longitude = '36.817223'

    maps_url = f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"

    return redirect(maps_url)    
    