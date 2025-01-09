from django.urls import path
from .views import *

urlpatterns = [
    path('projects/', ProjectListAPIView.as_view(), name="Project-list"),
    path('projects/<int:pk>/', ProjectDetailAPIView.as_view(), name="Project-detail"),
    
    path('tags/', TagListAPIView.as_view(), name="Tag-list"),
    path('tags/<int:pk>/', TagDetailAPIView.as_view(), name="Tag-detail"),

    path('category/', CategoryListAPIView.as_view(), name="Category-list"),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name="Category-detail"),

    path('status/', StatusListAPIView.as_view(), name="Status-list"),
    path('status/<int:pk>/', StatusDetailAPIView.as_view(), name="Status-detail"),

]
   