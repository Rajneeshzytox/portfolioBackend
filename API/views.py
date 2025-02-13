from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# import Models projects 
from .models import *

# import Serializers projects
from .serializers import *

############ FORCE SHELL COMMAND RUN
# from django.http import HttpResponse
# from django.core.management import call_command
# from django.contrib.auth import get_user_model

# def run_migrations(request):
#     call_command("migrate")
#     return HttpResponse("Migrations Applied!")

# def create_superuser(request):
#     User = get_user_model()
#     if not User.objects.filter(username="rajneesh").exists():
#         User.objects.create_superuser(
#             username="rajneesh",
#             email="rajneesh@admin.com",
#             password="admin123" 
#         )
#         return HttpResponse("Superuser Created! Use username: 'admin' and password: 'admin123'.")
#     else:
#         return HttpResponse("Superuser already exists.")

# HOMEM DATA FRONTEND
from .models import SocialLink, Experience, Education, AwardAndHonor, Skill, Resume, ResumeData
from .serializers import (
    SocialLinkSerializer,
    ExperienceSerializer,
    EducationSerializer,
    AwardAndHonorSerializer,
    SkillSerializer,
    ResumeSerializer,
    ResumeDataSerializer,
)

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




# ============ Home PAGE IF USER VISIT THE BACKEND  ===========
def home(req):
    return render(req, 'home.html')


########## -------------------- FRONTEND DATA ------------------------- ##########

class SocialLinkAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                link = SocialLink.objects.get(pk=pk)
                serializer = SocialLinkSerializer(link)
                return Response(serializer.data)
            except SocialLink.DoesNotExist:
                return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        links = SocialLink.objects.all()
        serializer = SocialLinkSerializer(links, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SocialLinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            link = SocialLink.objects.get(pk=pk)
            serializer = SocialLinkSerializer(link, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except SocialLink.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            link = SocialLink.objects.get(pk=pk)
            link.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except SocialLink.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)


# Similar structure for other models
class ExperienceAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                experience = Experience.objects.get(pk=pk)
                serializer = ExperienceSerializer(experience)
                return Response(serializer.data)
            except Experience.DoesNotExist:
                return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        experiences = Experience.objects.all()
        serializer = ExperienceSerializer(experiences, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ExperienceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            experience = Experience.objects.get(pk=pk)
            serializer = ExperienceSerializer(experience, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Experience.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            experience = Experience.objects.get(pk=pk)
            experience.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Experience.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)


# for Education,
class EducationAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                education = Education.objects.get(pk=pk)
                serializer = EducationSerializer(education)
                return Response(serializer.data)
            except Education.DoesNotExist:
                return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        educations = Education.objects.all()
        serializer = EducationSerializer(educations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EducationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            education = Education.objects.get(pk=pk)
            serializer = EducationSerializer(education, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Education.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            education = Education.objects.get(pk=pk)
            education.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Education.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
# AwardAndHonor,
class AwardAndHonorAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                data_object = AwardAndHonor.objects.get(pk=pk)
                serializer = AwardAndHonorSerializer(data_object)
                return Response(serializer.data)
            except AwardAndHonor.DoesNotExist:
                return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        data_objects = AwardAndHonor.objects.all()
        serializer = AwardAndHonorSerializer(data_objects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AwardAndHonorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            data_object = AwardAndHonor.objects.get(pk=pk)
            serializer = AwardAndHonorSerializer(data_object, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except AwardAndHonor.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            data_object = AwardAndHonor.objects.get(pk=pk)
            data_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except AwardAndHonor.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

# Skill,
class SkillAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                data_object = Skill.objects.get(pk=pk)
                serializer = SkillSerializer(data_object)
                return Response(serializer.data)
            except Skill.DoesNotExist:
                return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        data_objects = Skill.objects.all()
        serializer = SkillSerializer(data_objects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            data_object = Skill.objects.get(pk=pk)
            serializer = SkillSerializer(data_object, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Skill.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            data_object = Skill.objects.get(pk=pk)
            data_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Skill.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

# Resume,
class ResumeAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                data_object = Resume.objects.get(pk=pk)
                serializer = ResumeSerializer(data_object)
                return Response(serializer.data)
            except Resume.DoesNotExist:
                return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        data_objects = Resume.objects.all()
        serializer = ResumeSerializer(data_objects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ResumeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            data_object = Resume.objects.get(pk=pk)
            serializer = ResumeSerializer(data_object, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Resume.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            data_object = Resume.objects.get(pk=pk)
            data_object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Resume.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

# ResumeData
class ResumeDataAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                resume = ResumeData.objects.get(pk=pk)
                serializer = ResumeDataSerializer(resume)
                return Response(serializer.data)
            except ResumeData.DoesNotExist:
                return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        resumes = ResumeData.objects.all()
        serializer = ResumeDataSerializer(resumes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ResumeDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            resume = ResumeData.objects.get(pk=pk)
            serializer = ResumeDataSerializer(resume, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ResumeData.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            resume = ResumeData.objects.get(pk=pk)
            resume.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ResumeData.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)




# temp
from django.conf import settings
from django.http import HttpResponse
from django.conf.urls.static import static
def serve_media(request):
    try:
        with open(settings.MEDIA_ROOT / 'education_icons/mortarboard.png', 'rb') as f:
            return HttpResponse(f.read(), content_type="image/png")
    except FileNotFoundError:
        return HttpResponse("File not found", status=404)