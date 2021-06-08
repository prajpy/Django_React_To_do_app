from django.shortcuts import render
from .models import Task
from .serializers import Taskserializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def apiurlsoverview(request):
    api_urls = {
        'Tasklist-': '/Task-list/',
        'Taskdetail-': '/Task-detail/<str:pk>/',
        'Taskcreate-': '/Task-create/',
        'Taskupdate-': '/Task-update/<str:pk>/',
        'Taskdelete-': '/Task-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def tasklist(request):
    task = Task.objects.all()
    serializer = Taskserializers(task,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskdetail(request,pk):
    task = Task.objects.get(id=pk)
    serializer = Taskserializers(task,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createtaskview(request):
    serializer=Taskserializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updatetaskview(request,pk):
    task=Task.objects.get(id=pk)
    serializer = Taskserializers(data=request.data,instance=task)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deletetaskview(request,pk):
    task=Task.objects.get(id=pk)
    task.delete()
    return Response('record deleted successfully')
