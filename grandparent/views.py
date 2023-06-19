from django.shortcuts import render
from grandparent.models import Grandparent
# Create your views here.
from rest_framework import generics
from .serializers import GrandparentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def grandparent_list(request):
    if request.method == 'GET':
        grandparents = Grandparent.objects.all()
        serializer = GrandparentSerializer(grandparents,many=True)
        return Response(serializer.data)
    


@api_view(['GET'])
def grandparent_detail(request,pk):
    if request.method == 'GET':
        grandparent = Grandparent.objects.filter(pk=pk)
        serializer = GrandparentSerializer(grandparent,many=True)
        return Response(serializer.data)



@api_view(["POST"])
def grandparent_add(request):
    if request.method == "POST":
        serializer = GrandparentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['PATCH'])
def grandparent_update(request,pk):
    if request.method == 'PATCH':
        grandparent = Grandparent.objects.get(pk=pk)
        serializer = GrandparentSerializer(grandparent,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def grandparent_delete(request,pk):
    if request.method == 'DELETE':
        Grandparent.objects.get(pk=pk)
