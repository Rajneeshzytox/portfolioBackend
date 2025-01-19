from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# import Models 
from .models import *

# import Serializers
from .serializers import *

# ---------------- CRUD PROJECTS ---------------------\

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
           
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


## 2. Project Details (get, put, delete)
class ProjectDetailAPIView(APIView):
    def get(self, req, pk):
        try:
            project = Project.objects.get(id=pk)
            json = ProjectSerializer(project)
            return Response(json)
        
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, req, pk):
        project = Project.objects.get(id=pk)
        serializer = ProjectCreateSerializer(project, data=req.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, req, pk):
        try:
            project = Project.objects.get(id=pk)
            project.delete()
            
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            
            return Response(status=status.HTTP_404_NOT_FOUND)




## 1. Tag Create 
class TagListAPIView(APIView):
    def get(self, req):
        tags = Tag.objects.all()
        serialized_data = TagSerializer(tags, many=True)

        return Response(serialized_data.data)

    def post(self, req):
        
        post_data = TagSerializer(data=req.data)

        if post_data.is_valid():
            post_data.save()
            return Response(post_data.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)


## 2. Tag Details 
class TagDetailAPIView(APIView):
    def get(self, req, pk):
        try:
            tag = Tag.objects.get(id=pk)
            tag_data = TagSerializer(tag, many=False)
            return Response(tag_data.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, req, pk):
        try:

            tags = Tag.objects.get(id=pk)
            serializer = TagSerializer(tags, data=req.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)  
             

    def delete(self, req, pk):
        try:
            tag = Tag.objects.get(id=pk)
            tag.delete()
           
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
           
            return Response(status=status.HTTP_404_NOT_FOUND)

# -------------------- Categories ------------------

## 1. Category Create 
class CategoryListAPIView(APIView):
    def get(self, req):
        categories = Category.objects.all()

        serialized_data = CategorySerializer(categories, many=True)

        return Response(serialized_data.data)

    def post(self, req):
      
        category = CategorySerializer(data=req.data)
        
        if category.is_valid():
            category.save()
            return Response(category.data, status=status.HTTP_201_CREATED)
        return Response(status.HTTP_400_BAD_REQUEST)


## 2. Category Details 
class CategoryDetailAPIView(APIView):
    def get(self, req, pk):
        try:
            categories = Category.objects.get(id=pk)
            json = CategorySerializer(categories)
            return Response(json.data)
        
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, req, pk):
        try: 

            category = Category.objects.get(id=pk)
            serializer = CategorySerializer(category, data=req.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, req, pk):
        try:
            category = Category.objects.get(id=pk)
            category.delete()
           
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
           
            return Response(status=status.HTTP_404_NOT_FOUND)



## 1. Status Create 
class StatusListAPIView(APIView):
    def get(self, req):
        status = Status.objects.all()
        serialized_data = StatusSerializer(status, many=True)
        return Response(serialized_data.data)


    def post(self, req):
     
        status_data = StatusSerializer(data=req.data)
        if status_data.is_valid():
            status_data.save()
            return Response(status_data.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
## 2. Status Details 
class StatusDetailAPIView(APIView):
    def get(self, req, pk):
        try:
            status_data = Status.objects.get(id=pk)
            json = StatusSerializer(status_data)
            return Response(json.data)
        
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, req, pk):
        try: 
            status_data = Status.objects.get(id=pk)
            serializer = StatusSerializer(status_data, data=req.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, req, pk):
        try:
            status_data = Status.objects.get(id=pk)
            status_data.delete()
            
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            
            return Response(status=status.HTTP_404_NOT_FOUND)




# ============ Home ===========
def home(req):
    return render(req, 'home.html')





    


