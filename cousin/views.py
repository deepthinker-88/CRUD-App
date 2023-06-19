# Create your views here.
from .models import Cousin
from cousin.serializers import CousinSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

@api_view(["GET"])
def cousin_list(request):
    if request.method == "GET":
        cousin = Cousin.objects.all()
        serializer = CousinSerializer(cousin, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def cousin_detail(request, pk):
    if request.method == "GET":
        cousin = Cousin.objects.filter(pk=pk)
        serializer = CousinSerializer(cousin, many=True)
        return Response(serializer.data)


@api_view(["POST"])
def cousin_add(request):
    if request.method == "POST":
        serializer = CousinSerializer( data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PATCH"])
def CousinUpdate(request, pk):
    if request.method == "PATCH":
        cousin = Cousin.objects.get(pk=pk)
        serializer = CousinSerializer(cousin, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(["DELETE"])
def cousin_delete(request,pk):
    cousin = Cousin.objects.get(pk=pk)
    if request.method == "DELETE":
        cousin.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



