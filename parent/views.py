
from .serializers import ParentSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Parent


@api_view(['GET'])
def parent_list(request):
    if request.method == 'GET':
        parents = Parent.objects.all()
        serializer = ParentSerializer(parents,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def parent(request,pk):
    if request.method == 'GET':
        parent = Parent.objects.filter(pk=pk)
        serializer = ParentSerializer(parent,many=True)
        return Response(serializer.data)

@api_view(["POST"])
def parent_add(request):
    if request.method == "POST":
        serializer = ParentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["PATCH"])
def parent_update(request,pk):
    if request.method == "PATCH":
        parent = Parent.objects.get(pk=pk)
        serializer = ParentSerializer(parent,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def parent_delete(request,pk):
    if request.method == 'DELETE':
        parent = Parent.objects.get(pk=pk)
        parent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



