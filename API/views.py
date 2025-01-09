from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# import Models 
from .models import *

# import Serializers
from .serializers import *

# CRUD PROJECTS

## 1. Project Create (get, post)
class ProjectListAPIView(APIView):
    def get(self, req):
        projects = Project.objects.all()
        serialized = ProjectSerializer(projects, many=True)
        return Response(serialized.data)

    def post(self, req):
        serializer = ProjectCreateSerializer(data=req.data)

        if serializer.is_valid():
            project = serializer.save()
            # print("data is saved : \n", req.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # print("data wrong while project post: \n",req.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


## 2. Project Details (get, put, delete)
class ProjectDetailAPIView(APIView):
    def get(self, req, pk):
        pass

    def put(self, req, pk):
        project = Project.objects.get(id=pk)
        serializer = ProjectCreateSerializer(project, data=req.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, req, pk):
        try:
            project = Project.objects.get(id=pk)
            project.delete()
            # print("Project Deleted Successfully!")
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            # print("Not Found, DELETE Failed!")
            return Response(status.status.HTTP_404_NOT_FOUND)




## 1. Tag Create 
class TagListAPIView(APIView):
    def get(self, req):
        tags = Tag.objects.all()
        serialized_data = TagSerializer(tags, many=True)

        return Response(serialized_data.data)

    def post(self, req):
        pass


## 2. Tag Details 
class TagDetailAPIView(APIView):
    def get(self, req, pk):
        pass

    def put(self, req, pk):
        pass

    def delete(self, req, pk):
        pass



## 1. Category Create 
class CategoryListAPIView(APIView):
    def get(self, req):
        categories = Category.objects.all()

        serialized_data = CategorySerializer(categories, many=True)

        return Response(serialized_data.data)

    def post(self, req):
        pass


## 2. Category Details 
class CategoryDetailAPIView(APIView):
    def get(self, req, pk):
        pass

    def put(self, req, pk):
        pass

    def delete(self, req, pk):
        pass



## 1. Status Create 
class StatusListAPIView(APIView):
    def get(self, req):
        status = Status.objects.all()

        serialized_data = StatusSerializer(status, many=True)

        return Response(serialized_data.data)


    def post(self, req):
        pass

## 2. Status Details 
class StatusDetailAPIView(APIView):
    def get(self, req, pk):
        pass

    def put(self, req, pk):
        pass

    def delete(self, req, pk):
        pass










    


